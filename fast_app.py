import threading
import requests
from werkzeug.utils import secure_filename
from blueprintai.generate_model import generate_model
from fast_api_utils import verify_access_token, upload_model, get_asset_id, delete_asset, clear_folder
from glb_generator import create_empty_glb
from PIL import Image
from icecream import ic
import os

# New imports for FastAPI
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import (
    BaseModel,
    ValidationError,
    field_validator,
)
import uvicorn
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()
# Instrument the app
Instrumentator().instrument(app).expose(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://localhost:3000",
        "http://localhost:3000",
        "https://platform.hiverlab.com",
        "https://cloudexpo-tester.web.app",
        "https://ai-3dbp.hiverlab.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["Content-Type", "session-token"]
)

# Global set to track processing filenames
processing_files = set()
processing_lock = threading.Lock()

class Convert3DRequest(BaseModel):
    data: dict
    @field_validator('data')
    @classmethod
    def check_data(cls, data_posted):
        # Check if 'oss_ref' was provided
        oss_path = data_posted.get('oss_ref', None)
        if not oss_path:
            raise ValueError("oss_path is missing")
        
        # Check if group asset or personal asset
        group_asset = data_posted.get('isGroup', False)
        group_id = data_posted.get('groupID', None)

        if group_asset and not group_id:
            raise ValueError("Missing groupID when group_asset is True")
        
        return data_posted
            

@app.post('/convert-to-3d')
def convert_to_3d(request: Request, body: Convert3DRequest):
    try:
        # Check and verify Session token
        session_token = request.headers.get('session-token')
        if not session_token:
            raise HTTPException(status_code=401, detail="Session token is missing")
        if not verify_access_token(session_token):
            raise HTTPException(status_code=401, detail="Invalid access token")

        # Extract relevant fields from the 'data' dictionary
        data = body.data
        oss_path = data.get('oss_ref', None)
        group_asset = data.get('isGroup', False)
        group_id = data.get('groupID', None)
        fullURL = oss_path

        # extract image with link and saves as a variable.
        image = requests.get(fullURL, '').content

        # Check if file is already being processed
        with processing_lock:
            if image in processing_files:
                raise HTTPException(status_code=409, detail='File is already being processed')
            processing_files.add(fullURL)

        filename = os.path.basename(oss_path)
        ic(f"filename {filename}")
        output_file = 'result_' + filename.split('.')[0] + '.glb'
        ic(f"output file is generated now joining path together... {output_file}")
        glbOutput = output_file

        # Process the image in a separate thread
        def process_image():
            try:
                generate_model(image, fullURL)
            finally:
                with processing_lock:
                    processing_files.remove(fullURL)

        thread = threading.Thread(target=process_image)
        thread.start()
        thread.join()

        placeholder_id = get_asset_id(session_token, output_file)
        if placeholder_id and not delete_asset(session_token, placeholder_id):
            raise HTTPException(status_code=500, detail='Failed to delete placeholder model')

        if upload_model(glbOutput, session_token, group_asset, group_id):
            return {"err": False, "data": "Model uploaded successfully"}
        else:
            raise HTTPException(status_code=500, detail='Failed to upload model')

    except Exception as e:
        ic(f"Exception: {e}")
        with processing_lock:
            processing_files.remove(fullURL)  
        return JSONResponse(status_code=500, content={'err': True, 'data': str(e)})

def process_image(image, fullURL):
    try:
        generate_model(image, fullURL)
    finally:
        with processing_lock:
            processing_files.remove(fullURL)


from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

# Define the FastAPI app
app = FastAPI()

# Instrument the app for Prometheus
Instrumentator().instrument(app).expose(app)

# Define a simple data model for the POST request
class Message(BaseModel):
    content: str

# Define a POST endpoint
@app.post("/hello")
def hello_world(message: Message):
    return {"message": "Hello World"}
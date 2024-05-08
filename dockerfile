# Use an official Python runtime as a parent image
FROM python:3.10.4-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local directory contents into the container at /app
COPY . /app

# Install any needed packages
RUN pip install --no-cache-dir fastapi uvicorn gunicorn pydantic prometheus_fastapi_instrumentator

# Expose the port the app runs on
EXPOSE 8000

# Define environment variable for the module where the FastAPI app is defined
ENV MODULE_NAME="fast_app"

# Run the application using Gunicorn with Uvicorn workers
CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "$MODULE_NAME:app", "--bind", "0.0.0.0:8000"]

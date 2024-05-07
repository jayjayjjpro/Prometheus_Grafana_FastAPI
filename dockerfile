# Start from a specific version of the official Python image
FROM python:3.10.4-slim

# Install necessary libraries for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-dev \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file and the cython constraint file into the container
COPY requirements.txt cython_constraint.txt ./

# Install any needed packages specified in requirements.txt using the constraint file
RUN PIP_CONSTRAINT=cython_constraint.txt pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Command to run the application using Gunicorn with Uvicorn workers
CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "wsgi:app", "--bind", "0.0.0.0:8000"]


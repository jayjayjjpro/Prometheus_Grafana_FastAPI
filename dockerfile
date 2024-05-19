# Start from a specific version of the official Python image
FROM python:3.10.4-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Make the port available to the world outside this container
EXPOSE ${WEB_CONTAINER_PORT}

# Set environment variables
ENV WEB_CONTAINER_PORT=${WEB_CONTAINER_PORT}

# Command to run the application using Gunicorn with Uvicorn workers
CMD ["sh", "-c", "gunicorn -w 1 -k uvicorn.workers.UvicornWorker wsgi:app --bind 0.0.0.0:${WEB_CONTAINER_PORT}"]

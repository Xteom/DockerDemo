# Use the official JupyterLab image as the base image
FROM jupyter/datascience-notebook:latest

# Set the working directory
WORKDIR /home/jovyan

# Copy the requirements.txt file into the container
COPY requirements.txt .
COPY keys.py .

# Install custom dependencies
RUN pip install --no-cache-dir -r requirements.txt
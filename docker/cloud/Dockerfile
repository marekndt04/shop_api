# Use an official Python image as the base image
FROM python:3.11-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements/base.txt .

# Install the required packages
RUN pip install --no-cache-dir -r local.txt

# Copy the rest of the application files to the container
COPY . .

# Set the environment variable for the application entry point
ENV PYTHONUNBUFFERED 1
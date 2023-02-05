# Use an official Python image as the base image
FROM python:3.11-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Create a group and user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Tell docker that all future commands should run as the appuser user
USER appuser


# Copy the requirements.txt file to the container
COPY requirements/local.txt .

# Install the required packages
RUN pip install --no-cache-dir -r local.txt

# Copy the rest of the application files to the container
COPY . .

# Set the environment variable for the application entry point
ENV PYTHONUNBUFFERED 1
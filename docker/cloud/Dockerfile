# Use an official Python image as the base image
FROM python:3.11-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

#VSCode development vith devcontainers
RUN apt update && apt install -y sudo && apt -y install git

ARG USERNAME=appuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID

## Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Copy the requirements.txt file to the container
COPY requirements/cloud.txt .

# Install the required packages
RUN pip install --no-cache-dir -r cloud.txt

# Copy the rest of the application files to the container
COPY . .

# Set the environment variable for the application entry point
ENV PYTHONUNBUFFERED 1
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt .
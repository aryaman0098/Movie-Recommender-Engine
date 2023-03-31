# Use the official Python image as the base image
FROM python:3.9.6

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

# Install the application dependencies
RUN pip3 install -r requirements.txt

EXPOSE 3000

# Define the entry point for the container
CMD python3 ./app.py
# Use an official Python runtime as a parent image
FROM python:slim-bookworm

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requierements.txt

# Run app.py when the container launches
CMD ["python", "motd-api.py"]
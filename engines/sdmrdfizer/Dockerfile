# Use an official Python runtime as a parent image
FROM python:3

RUN apt-get update && apt-get install -y htop vim bc unzip

# Set the working directory to /sdmrdfizer
WORKDIR /sdmrdfizer

# Copy the current directory contents into the container at /sdmrdfizer
COPY . /sdmrdfizer

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r /sdmrdfizer/requirements.txt

# Run app.py when the container launches
CMD ["tail", "-f", "/dev/null"]


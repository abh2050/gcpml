FROM python:3.8-slim

# Set a directory for the app inside the Docker container
WORKDIR /app

# Copy all the files from the current directory to the container's working directory
COPY . .

# Install dependencies
RUN pip install openai==0.28

# Make port available to the world outside this container
EXPOSE 8080

# Command to run the application
CMD ["python", "./main.py"]


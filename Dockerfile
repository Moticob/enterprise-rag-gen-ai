# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the necessary dependencies
RUN pip install -r backend/requirements.txt

# Expose the port Streamlit will run on
EXPOSE 8501

# Set the environment variable for the Streamlit server port
ENV STREAMLIT_SERVER_PORT 8501

# Run the Streamlit app
CMD ["streamlit", "run", "frontend/app.py"]


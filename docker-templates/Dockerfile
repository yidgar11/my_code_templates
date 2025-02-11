FROM python:3.9-slim
# Choose a minimal base image (e.g., Alpine Linux) to reduce the size
# of the final image and minimize vulnerabilities

# Add metadata about the image
LABEL maintainer="your_email@example.com"

# Set the working directory inside the container
WORKDIR /app

# Copy files from the host to the container
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# declare that a container listens on specific network ports at runtime
EXPOSE 5000

# use ENV to update the PATH environment variable for the software your container installs
ENV DB_HOST=localhost
ENV DB_NAME=mydatabase
ENV DB_USER=myuser
ENV DB_PASSWORD=mypassword


# Define the command to run when the container starts
CMD ["python", "app.py"]

# An ENTRYPOINT allows you to configure a container that will run as an executable.
ENTRYPOINT ["executable", "param1", "param2"]


# Avoid running containers as root.
# Create a non-root user and switch to it using `USER` in the Dockerfile
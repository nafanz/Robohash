FROM debian:12-slim

# Set environment variables
ENV PORT=8080
ENV PYTHONUNBUFFERED=1

# Install system dependencies in a single layer to reduce image size
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-pillow \
    python3-tornado \
    python3-natsort \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the application code
COPY robohash/ /app/robohash/
COPY setup.py .
COPY README.md .

# Install the application in development mode
# Use the --break-system-packages flag since this is a controlled environment
RUN pip3 install -e . --break-system-packages

# Expose the port that the application will run on
EXPOSE 8080

# Command to run the application
CMD ["python3", "-m", "robohash.webfront"]
#!/usr/bin/env bash

# Build the Docker image only if necessary
if [[ "$(docker images -q sys-lab-1_image 2> /dev/null)" == "" ]]; then
    echo "Building Docker image..."
    docker build --progress=plain -t sys-lab-1_image .
fi

# Remove any existing container with the same name (running or exited)
if [[ "$(docker ps -a -q -f name=^/sys-lab-1_container$)" ]]; then
    echo "Removing existing container sys-lab-1_container..."
    docker rm -f sys-lab-1_container
fi

# Start the container
echo "Starting Docker container..."
docker run -d --name sys-lab-1_container \
    --mount type=bind,source=/home/sebek/sandbox/practice/jason/labs/systems-lab-1,target=/workspaces/sys-lab-1 \
    sys-lab-1_image sleep infinity

#!/usr/bin/env bash

# Build the Docker image only if necessary
if [[ "$(docker images -q sys-lab-1_image 2> /dev/null)" == "" ]]; then
    echo "Building Docker image..."
    docker build --progress=plain -t sys-lab-1_image .
fi

# Check if the container is already running
if [[ "$(docker ps -q -f name=sys-lab-1_container)" ]]; then
    echo "Container is already running."
else
    echo "Starting Docker container..."
    docker run -d --name sys-lab-1_container \
        --mount type=bind,source=/Users/jason/sandbox/practice/jason/labs/systems-lab-1,target=/workspaces/sys-lab-1,readonly \
        sys-lab-1_image
fi

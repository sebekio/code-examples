#!/usr/bin/env bash

docker build --progress=plain -t sys-lab-1_image . && \
docker run -d --name sys-labs1_container \
    --mount type=bind,source=/Users/jason/sandbox/practice/jason/labs/systems-lab-1,target=/workspaces/sys-lab-1,readonly \
    sys-lab-1_image

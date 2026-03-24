FROM ubuntu:noble

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    autoconf automake autotools-dev curl python3 python3-pip python3-tomli \
    libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo \
    gperf libtool patchutils bc zlib1g-dev libexpat-dev ninja-build git cmake \
    libglib2.0-dev libslirp-dev libncurses-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Clone and build RISC-V toolchain
RUN git clone https://github.com/riscv/riscv-gnu-toolchain /tmp/riscv && \
    cd /tmp/riscv && \
    ./configure --prefix=/opt/riscv && \
    make linux -j$(nproc) && \
    rm -rf /tmp/riscv

# Set up workspace
RUN mkdir -p /workspaces/sys-lab-1
WORKDIR /workspaces/sys-lab-1

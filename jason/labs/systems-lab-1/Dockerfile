FROM ubuntu:noble

# base image for risc-v gnu toolchain
RUN apt-get update && apt-get install -y --no-install-recommends \
autoconf automake autotools-dev curl python3 python3-pip python3-tomli libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev ninja-build git cmake libglib2.0-dev libslirp-dev libncurses-dev

RUN which git >/dev/null 2>&1 && git clone https://github.com/riscv/riscv-gnu-toolchain /tmp/riscv

RUN ls -1a /tmp/riscv

RUN /tmp/riscv/configure --prefix=/opt/riscv && make linux -j$(nproc)

# installation of build-essentials
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential

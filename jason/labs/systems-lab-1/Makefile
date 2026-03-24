SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

PROJ_DIR = /workspaces/sys-lab-1
BUILD_CPP_DIR = $(PROJ_DIR)/build_cpp
BUILD_C_DIR = $(PROJ_DIR)/build_c
BUILD_RISCV_DIR = $(PROJ_DIR)/build_riscv

.PHONY: all cpp c test_cpp test_c clean

all: cpp c

cpp: | $(BUILD_CPP_DIR)
>g++ -g $(PROJ_DIR)/cell.cpp -o $(BUILD_CPP_DIR)/cell

c: | $(BUILD_C_DIR)
>gcc -g $(PROJ_DIR)/cell.c -o $(BUILD_C_DIR)/cell

test_cpp: | $(BUILD_CPP_DIR)
>g++ -g $(PROJ_DIR)/cell.cpp $(PROJ_DIR)/test_cell.cpp -o $(BUILD_CPP_DIR)/test_cell
>$(BUILD_CPP_DIR)/test_cell

test_c: | $(BUILD_C_DIR)
>gcc -g $(PROJ_DIR)/cell.c $(PROJ_DIR)/test_cell.c -o $(BUILD_C_DIR)/test_cell
>$(BUILD_C_DIR)/test_cell

# build recipe for riscv
$(BUILD_RISCV_DIR)/cell: $(PROJ_DIR)/cell_rv.s | $(BUILD_RISCV_DIR)
>riscv64-unknown-elf-gcc -o $(BUILD_RISCV_DIR)/cell $(PROJ_DIR)/cell_rv.s

$(BUILD_CPP_DIR) $(BUILD_C_DIR) $(BUILD_RISCV_DIR):
>mkdir -p $@

clean:
>rm -rf $(BUILD_CPP_DIR) $(BUILD_C_DIR) $(BUILD_RISCV_DIR)
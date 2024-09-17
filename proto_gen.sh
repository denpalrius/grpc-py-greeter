#!/bin/bash

# Variables
PROTO_FILE="./proto/greeter.proto"
PROTO_PATH="./proto"
OUTDIR="./proto/schema"

# Create output directory
mkdir -p ${OUTDIR}

# Generate Python code
python -m grpc_tools.protoc \
    --python_out=${OUTDIR} \
    --pyi_out=${OUTDIR} \
    --grpc_python_out=${OUTDIR} \
    --proto_path=${PROTO_PATH} \
    ${PROTO_FILE}

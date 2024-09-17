#!/bin/bash

# Variables
PROTO_FILE="./proto/greeter.proto"
PROTO_PATH="./proto"
OUTDIR="./proto/schema"

# Create output directory
mkdir -p ${OUTDIR}

# Generate Python code
echo -e "\nGenerating gRPC Python files..."
python -m grpc_tools.protoc \
    --python_out=${OUTDIR} \
    --pyi_out=${OUTDIR} \
    --grpc_python_out=${OUTDIR} \
    --proto_path=${PROTO_PATH} \
    ${PROTO_FILE}

# Check if the gRPC generation was successful
if [ $? -ne 0 ]; then
    echo -e "\nError: gRPC file generation failed"
    exit 1
fi

# Run the Python script to adjust imports
echo -e "\nAdjusting imports in generated Python files..."
python3 ./proto/adjust_grpc_imports.py

# Check if the Python script ran successfully
if [ $? -ne 0 ]; then
    echo -e "\nError: Import adjustment failed"
    exit 1
fi

echo -e "\ngRPC file generation and import adjustment completed successfully."
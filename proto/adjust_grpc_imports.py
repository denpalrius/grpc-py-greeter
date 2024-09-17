#!/usr/bin/env python3

import os
import re

def adjust_imports(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Adjust the import statement
    content = re.sub(
        r'import greeter_pb2 as greeter__pb2',
        'import proto.schema.greeter_pb2 as greeter__pb2',
        content
    )

    with open(file_path, 'w') as file:
        file.write(content)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('_pb2_grpc.py'):
                file_path = os.path.join(root, file)
                adjust_imports(file_path)
                print(f"Adjusted imports in {file_path}")

if __name__ == "__main__":
    proto_dir = "./proto/schema"
    process_directory(proto_dir)
    print("Import adjustments completed.")
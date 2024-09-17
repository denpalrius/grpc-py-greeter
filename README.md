# gRPC Python Greeter
A simple gRPC service implemented in Python to demonstrate the use of gRPC for communication between a client and server. This project includes both server and client implementations for a basic "Greeter" service.

## Features

- Basic gRPC server and client setup
- Simple "Greeter" service with methods to send and receive greetings
- Demonstrates how to define gRPC services using Protocol Buffers

## Getting Started

These instructions will help you set up and run the gRPC server and client on your local machine.

### Prerequisites

- Python 3.11 or higher
- `pip` for package management

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/denpalrius/grpc-py-greeter.git
    cd grpc-py-greeter
    ```

2. Install dependencies using Poetry:

    ```bash
    # Ensure Poetry is installed (pip install poetry)
    poetry install
    ```

   Alternatively, if you prefer to use `pip`, you can install the dependencies directly:

    ```bash
    pip install grpcio==1.66.1 grpcio-tools==1.54.0
    ```

3. Compile the Protocol Buffers files using the provided script:

    ```bash
    ./proto_gen.sh
    ```

    This will generate the required Python files in the `./proto/schema` directory.

### Running the Server

To start the gRPC server, run:

```bash
poetry run python hello_server.py
```

or

```bash
python hello_server.py
```

The server will start and listen for incoming gRPC requests.

### Running the Client

To run the gRPC client and send a request to the server, run:

```bash
poetry run python hello_client.py
```
or

```bash
python hello_client.py
```

### Usage

1. **Start the server** by running the `hello_server.py` script.
2. **Run the client** by executing the `hello_client.py` script to send a greeting request to the server and receive a response.

## Acknowledgements

- [gRPC](https://grpc.io/) - A high-performance, open-source universal RPC framework that enables efficient communication between distributed systems.
- [gRPC Python Quickstart](https://grpc.io/docs/languages/python/quickstart/) - A guide to quickly get started with gRPC in Python, including installation and basic usage.
- [gRPC Python API Reference](https://grpc.github.io/grpc/python/) - Comprehensive documentation for the gRPC Python API, detailing all available classes and methods.
- [Protocol Buffers](https://developers.google.com/protocol-buffers) - Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data, used to define gRPC services.
- [Poetry](https://python-poetry.org/) - A tool for dependency management and packaging in Python, simplifying the process of managing project dependencies and virtual environments.

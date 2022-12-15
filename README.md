# protobuf-grpc-distutils-example

This repo provides an example of how to use [protobuf-grpc-distutils](https://github.com/idex-biometrics/protobuf-grpc-distutils) to share
a common protobuf repository between multiple Python projects.

The issue of generating the Python protobuf outputs has been discussed in a number of tickets including
[protobuf/1491](https://github.com/protocolbuffers/protobuf/issues/1491).  The main issue stems from the fact
that the generated Python modules don't obey the Python3 import rules: [comment](https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-262968397).

## Running the example

When you pip install the package, the Python protobuf and gRPC outputs will be generated and will be available in the `helloworld` package.

```
$ python3 -m venv venv
$ . ./venv/bin/activate
$ pip install git+https://github.com/idex-biometrics/protobuf-grpc-distutils-example
```

You will also have two command line scripts on your path that provide a simple gRPC example.  Run the `hello_server` in one terminal window
and then run `hello_client` in another.

## A note on Python package names

As noted in [this comment](https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-1137868304), it is possible to get the `protoc`
compiler to generate the Python modules with the correct import hierarchy if you structure your proto hierarchy to match.  In this case the required
Python package is `helloworld` and the `src` directory contains a placeholder along with the command line scripts.

```
src/
└── helloworld
    ├── __init__.py
    ├── client.py
    └── server.py
```

The `proto` directory structure matches this:

```
proto/
└── helloworld
    └── hello.proto
```

and following installation, the directory under your `venv` will look like:

```
venv/lib/python3.10/site-packages/helloworld/
├── __init__.py
├── _version.py
├── client.py
├── hello_pb2.py
├── hello_pb2_grpc.py
└── server.py
```

where the `hello_pb2_grpc.py` module has the correct import statement:

```
$ grep import venv/lib/python3.10/site-packages/helloworld/hello_pb2_grpc.py
import grpc
from helloworld import hello_pb2 as helloworld_dot_hello__pb2
```

There are other ways of fixing the incorrect import paths such as hacking `sys.path` or post processing the generated
files.  The `protoc` compiler also seems to accept more complex arguments passed to `--proto-path` as detailed in 
[this comment](https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-1279336064).
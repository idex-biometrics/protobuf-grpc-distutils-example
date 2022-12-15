#!/usr/bin/env python3

import sys
import grpc
import helloworld.hello_pb2 as helloworld_pb2
import helloworld.hello_pb2_grpc as helloworld_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message)

if __name__ == "__main__":
    sys.exit(run())
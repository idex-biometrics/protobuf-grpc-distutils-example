import setuptools
import setuptools.command.build

setuptools.command.build.build.sub_commands.insert(0, ('generate_grpc_py_protobufs', None))
setuptools.setup(
    options={
        'generate_grpc_py_protobufs': {
            'source_dir':        './proto',
            'proto_root_path':   './proto',
            'extra_proto_paths': [],
            'output_dir':        './src',
            'proto_files':       [
                './proto/helloworld/hello.proto',
            ],
        }
    }
)
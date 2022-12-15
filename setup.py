import setuptools
import setuptools.command.build

setuptools.command.build.build.sub_commands.insert(0, ('generate_grpc_py_protobufs', None))
setuptools.setup(
    options={
        'generate_grpc_py_protobufs': {
            'source_dir':        '.',
            'proto_root_path':   '.',
            'extra_proto_paths': [],
            'output_dir':        '.',
            # 'output_dir':        './src/genesee_protobuf',
            'proto_files':       [
                './proto/hello.proto',
            ],
        }
    }
)
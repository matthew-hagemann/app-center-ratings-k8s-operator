# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import ratings_features_user_pb2 as ratings__features__user__pb2


class UserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Authenticate = channel.unary_unary(
                '/ratings.features.user.User/Authenticate',
                request_serializer=ratings__features__user__pb2.AuthenticateRequest.SerializeToString,
                response_deserializer=ratings__features__user__pb2.AuthenticateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/ratings.features.user.User/Delete',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Vote = channel.unary_unary(
                '/ratings.features.user.User/Vote',
                request_serializer=ratings__features__user__pb2.VoteRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ListMyVotes = channel.unary_unary(
                '/ratings.features.user.User/ListMyVotes',
                request_serializer=ratings__features__user__pb2.ListMyVotesRequest.SerializeToString,
                response_deserializer=ratings__features__user__pb2.ListMyVotesResponse.FromString,
                )
        self.GetSnapVotes = channel.unary_unary(
                '/ratings.features.user.User/GetSnapVotes',
                request_serializer=ratings__features__user__pb2.GetSnapVotesRequest.SerializeToString,
                response_deserializer=ratings__features__user__pb2.GetSnapVotesResponse.FromString,
                )


class UserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Authenticate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Vote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMyVotes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSnapVotes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Authenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.Authenticate,
                    request_deserializer=ratings__features__user__pb2.AuthenticateRequest.FromString,
                    response_serializer=ratings__features__user__pb2.AuthenticateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Vote': grpc.unary_unary_rpc_method_handler(
                    servicer.Vote,
                    request_deserializer=ratings__features__user__pb2.VoteRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListMyVotes': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMyVotes,
                    request_deserializer=ratings__features__user__pb2.ListMyVotesRequest.FromString,
                    response_serializer=ratings__features__user__pb2.ListMyVotesResponse.SerializeToString,
            ),
            'GetSnapVotes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSnapVotes,
                    request_deserializer=ratings__features__user__pb2.GetSnapVotesRequest.FromString,
                    response_serializer=ratings__features__user__pb2.GetSnapVotesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ratings.features.user.User', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class User(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Authenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ratings.features.user.User/Authenticate',
            ratings__features__user__pb2.AuthenticateRequest.SerializeToString,
            ratings__features__user__pb2.AuthenticateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ratings.features.user.User/Delete',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Vote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ratings.features.user.User/Vote',
            ratings__features__user__pb2.VoteRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMyVotes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ratings.features.user.User/ListMyVotes',
            ratings__features__user__pb2.ListMyVotesRequest.SerializeToString,
            ratings__features__user__pb2.ListMyVotesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSnapVotes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ratings.features.user.User/GetSnapVotes',
            ratings__features__user__pb2.GetSnapVotesRequest.SerializeToString,
            ratings__features__user__pb2.GetSnapVotesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

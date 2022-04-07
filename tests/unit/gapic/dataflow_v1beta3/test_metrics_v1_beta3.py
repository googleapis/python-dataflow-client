# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import mock

import grpc
from grpc.experimental import aio
import math
import pytest
from proto.marshal.rules.dates import DurationRule, TimestampRule


from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import path_template
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.dataflow_v1beta3.services.metrics_v1_beta3 import (
    MetricsV1Beta3AsyncClient,
)
from google.cloud.dataflow_v1beta3.services.metrics_v1_beta3 import MetricsV1Beta3Client
from google.cloud.dataflow_v1beta3.services.metrics_v1_beta3 import pagers
from google.cloud.dataflow_v1beta3.services.metrics_v1_beta3 import transports
from google.cloud.dataflow_v1beta3.types import metrics
from google.oauth2 import service_account
from google.protobuf import timestamp_pb2  # type: ignore
import google.auth


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert MetricsV1Beta3Client._get_default_mtls_endpoint(None) is None
    assert (
        MetricsV1Beta3Client._get_default_mtls_endpoint(api_endpoint)
        == api_mtls_endpoint
    )
    assert (
        MetricsV1Beta3Client._get_default_mtls_endpoint(api_mtls_endpoint)
        == api_mtls_endpoint
    )
    assert (
        MetricsV1Beta3Client._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        MetricsV1Beta3Client._get_default_mtls_endpoint(sandbox_mtls_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        MetricsV1Beta3Client._get_default_mtls_endpoint(non_googleapi) == non_googleapi
    )


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (MetricsV1Beta3Client, "grpc"),
        (MetricsV1Beta3AsyncClient, "grpc_asyncio"),
    ],
)
def test_metrics_v1_beta3_client_from_service_account_info(
    client_class, transport_name
):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_info"
    ) as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info, transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == ("dataflow.googleapis.com:443")


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.MetricsV1Beta3GrpcTransport, "grpc"),
        (transports.MetricsV1Beta3GrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
def test_metrics_v1_beta3_client_service_account_always_use_jwt(
    transport_class, transport_name
):
    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (MetricsV1Beta3Client, "grpc"),
        (MetricsV1Beta3AsyncClient, "grpc_asyncio"),
    ],
)
def test_metrics_v1_beta3_client_from_service_account_file(
    client_class, transport_name
):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file(
            "dummy/file/path.json", transport=transport_name
        )
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json(
            "dummy/file/path.json", transport=transport_name
        )
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == ("dataflow.googleapis.com:443")


def test_metrics_v1_beta3_client_get_transport_class():
    transport = MetricsV1Beta3Client.get_transport_class()
    available_transports = [
        transports.MetricsV1Beta3GrpcTransport,
    ]
    assert transport in available_transports

    transport = MetricsV1Beta3Client.get_transport_class("grpc")
    assert transport == transports.MetricsV1Beta3GrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (MetricsV1Beta3Client, transports.MetricsV1Beta3GrpcTransport, "grpc"),
        (
            MetricsV1Beta3AsyncClient,
            transports.MetricsV1Beta3GrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
    ],
)
@mock.patch.object(
    MetricsV1Beta3Client,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(MetricsV1Beta3Client),
)
@mock.patch.object(
    MetricsV1Beta3AsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(MetricsV1Beta3AsyncClient),
)
def test_metrics_v1_beta3_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(MetricsV1Beta3Client, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(MetricsV1Beta3Client, "get_transport_class") as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class(transport=transport_name)

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}
    ):
        with pytest.raises(ValueError):
            client = client_class(transport=transport_name)

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,use_client_cert_env",
    [
        (MetricsV1Beta3Client, transports.MetricsV1Beta3GrpcTransport, "grpc", "true"),
        (
            MetricsV1Beta3AsyncClient,
            transports.MetricsV1Beta3GrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (MetricsV1Beta3Client, transports.MetricsV1Beta3GrpcTransport, "grpc", "false"),
        (
            MetricsV1Beta3AsyncClient,
            transports.MetricsV1Beta3GrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
    ],
)
@mock.patch.object(
    MetricsV1Beta3Client,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(MetricsV1Beta3Client),
)
@mock.patch.object(
    MetricsV1Beta3AsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(MetricsV1Beta3AsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_metrics_v1_beta3_client_mtls_env_auto(
    client_class, transport_class, transport_name, use_client_cert_env
):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        options = client_options.ClientOptions(
            client_cert_source=client_cert_source_callback
        )
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client.DEFAULT_ENDPOINT
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=True,
            ):
                with mock.patch(
                    "google.auth.transport.mtls.default_client_cert_source",
                    return_value=client_cert_source_callback,
                ):
                    if use_client_cert_env == "false":
                        expected_host = client.DEFAULT_ENDPOINT
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class(transport=transport_name)
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=False,
            ):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                )


@pytest.mark.parametrize(
    "client_class", [MetricsV1Beta3Client, MetricsV1Beta3AsyncClient]
)
@mock.patch.object(
    MetricsV1Beta3Client,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(MetricsV1Beta3Client),
)
@mock.patch.object(
    MetricsV1Beta3AsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(MetricsV1Beta3AsyncClient),
)
def test_metrics_v1_beta3_client_get_mtls_endpoint_and_cert_source(client_class):
    mock_client_cert_source = mock.Mock()

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "true".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source == mock_client_cert_source

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "false".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
        mock_client_cert_source = mock.Mock()
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert doesn't exist.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=False,
        ):
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
            assert api_endpoint == client_class.DEFAULT_ENDPOINT
            assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert exists.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=True,
        ):
            with mock.patch(
                "google.auth.transport.mtls.default_client_cert_source",
                return_value=mock_client_cert_source,
            ):
                (
                    api_endpoint,
                    cert_source,
                ) = client_class.get_mtls_endpoint_and_cert_source()
                assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
                assert cert_source == mock_client_cert_source


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (MetricsV1Beta3Client, transports.MetricsV1Beta3GrpcTransport, "grpc"),
        (
            MetricsV1Beta3AsyncClient,
            transports.MetricsV1Beta3GrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
    ],
)
def test_metrics_v1_beta3_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(
        scopes=["1", "2"],
    )
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,grpc_helpers",
    [
        (
            MetricsV1Beta3Client,
            transports.MetricsV1Beta3GrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            MetricsV1Beta3AsyncClient,
            transports.MetricsV1Beta3GrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_metrics_v1_beta3_client_client_options_credentials_file(
    client_class, transport_class, transport_name, grpc_helpers
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")

    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


def test_metrics_v1_beta3_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.dataflow_v1beta3.services.metrics_v1_beta3.transports.MetricsV1Beta3GrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = MetricsV1Beta3Client(
            client_options={"api_endpoint": "squid.clam.whelk"}
        )
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,grpc_helpers",
    [
        (
            MetricsV1Beta3Client,
            transports.MetricsV1Beta3GrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            MetricsV1Beta3AsyncClient,
            transports.MetricsV1Beta3GrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_metrics_v1_beta3_client_create_channel_credentials_file(
    client_class, transport_class, transport_name, grpc_helpers
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")

    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

    # test that the credentials from file are saved and used as the credentials.
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel"
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        file_creds = ga_credentials.AnonymousCredentials()
        load_creds.return_value = (file_creds, None)
        adc.return_value = (creds, None)
        client = client_class(client_options=options, transport=transport_name)
        create_channel.assert_called_with(
            "dataflow.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/compute.readonly",
                "https://www.googleapis.com/auth/userinfo.email",
            ),
            scopes=None,
            default_host="dataflow.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        metrics.GetJobMetricsRequest,
        dict,
    ],
)
def test_get_job_metrics(request_type, transport: str = "grpc"):
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_job_metrics), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = metrics.JobMetrics()
        response = client.get_job_metrics(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == metrics.GetJobMetricsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, metrics.JobMetrics)


def test_get_job_metrics_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_job_metrics), "__call__") as call:
        client.get_job_metrics()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == metrics.GetJobMetricsRequest()


@pytest.mark.asyncio
async def test_get_job_metrics_async(
    transport: str = "grpc_asyncio", request_type=metrics.GetJobMetricsRequest
):
    client = MetricsV1Beta3AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_job_metrics), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(metrics.JobMetrics())
        response = await client.get_job_metrics(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == metrics.GetJobMetricsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, metrics.JobMetrics)


@pytest.mark.asyncio
async def test_get_job_metrics_async_from_dict():
    await test_get_job_metrics_async(request_type=dict)


@pytest.mark.parametrize(
    "request_type",
    [
        metrics.GetJobExecutionDetailsRequest,
        dict,
    ],
)
def test_get_job_execution_details(request_type, transport: str = "grpc"):
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_job_execution_details), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = metrics.JobExecutionDetails(
            next_page_token="next_page_token_value",
        )
        response = client.get_job_execution_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == metrics.GetJobExecutionDetailsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.GetJobExecutionDetailsPager)
    assert response.next_page_token == "next_page_token_value"


def test_get_job_execution_details_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_job_execution_details), "__call__"
    ) as call:
        client.get_job_execution_details()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == metrics.GetJobExecutionDetailsRequest()


@pytest.mark.asyncio
async def test_get_job_execution_details_async(
    transport: str = "grpc_asyncio", request_type=metrics.GetJobExecutionDetailsRequest
):
    client = MetricsV1Beta3AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_job_execution_details), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            metrics.JobExecutionDetails(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.get_job_execution_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == metrics.GetJobExecutionDetailsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.GetJobExecutionDetailsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.asyncio
async def test_get_job_execution_details_async_from_dict():
    await test_get_job_execution_details_async(request_type=dict)


def test_get_job_execution_details_pager(transport_name: str = "grpc"):
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_job_execution_details), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            metrics.JobExecutionDetails(
                stages=[
                    metrics.StageSummary(),
                    metrics.StageSummary(),
                    metrics.StageSummary(),
                ],
                next_page_token="abc",
            ),
            metrics.JobExecutionDetails(
                stages=[],
                next_page_token="def",
            ),
            metrics.JobExecutionDetails(
                stages=[
                    metrics.StageSummary(),
                ],
                next_page_token="ghi",
            ),
            metrics.JobExecutionDetails(
                stages=[
                    metrics.StageSummary(),
                    metrics.StageSummary(),
                ],
            ),
            RuntimeError,
        )

        metadata = ()
        pager = client.get_job_execution_details(request={})

        assert pager._metadata == metadata

        results = [i for i in pager]
        assert len(results) == 6
        assert all(isinstance(i, metrics.StageSummary) for i in results)


def test_get_job_execution_details_pages(transport_name: str = "grpc"):
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_job_execution_details), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            metrics.JobExecutionDetails(
                stages=[
                    metrics.StageSummary(),
                    metrics.StageSummary(),
                    metrics.StageSummary(),
                ],
                next_page_token="abc",
            ),
            metrics.JobExecutionDetails(
                stages=[],
                next_page_token="def",
            ),
            metrics.JobExecutionDetails(
                stages=[
                    metrics.StageSummary(),
                ],
                next_page_token="ghi",
            ),
            metrics.JobExecutionDetails(
                stages=[
                    metrics.StageSummary(),
                    metrics.StageSummary(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.get_job_execution_details(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_get_job_execution_details_async_pager():
    client = MetricsV1Beta3AsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_job_execution_details),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            metrics.JobExecutionDetails(
                stages=[
                    metrics.StageSummary(),
                    metrics.StageSummary(),
                    metrics.StageSummary(),
                ],
                next_page_token="abc",
            ),
            metrics.JobExecutionDetails(
                stages=[],
                next_page_token="def",
            ),
            metrics.JobExecutionDetails(
                stages=[
                    metrics.StageSummary(),
                ],
                next_page_token="ghi",
            ),
            metrics.JobExecutionDetails(
                stages=[
                    metrics.StageSummary(),
                    metrics.StageSummary(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.get_job_execution_details(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, metrics.StageSummary) for i in responses)


@pytest.mark.asyncio
async def test_get_job_execution_details_async_pages():
    client = MetricsV1Beta3AsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_job_execution_details),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            metrics.JobExecutionDetails(
                stages=[
                    metrics.StageSummary(),
                    metrics.StageSummary(),
                    metrics.StageSummary(),
                ],
                next_page_token="abc",
            ),
            metrics.JobExecutionDetails(
                stages=[],
                next_page_token="def",
            ),
            metrics.JobExecutionDetails(
                stages=[
                    metrics.StageSummary(),
                ],
                next_page_token="ghi",
            ),
            metrics.JobExecutionDetails(
                stages=[
                    metrics.StageSummary(),
                    metrics.StageSummary(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.get_job_execution_details(request={})
        ).pages:  # pragma: no branch
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        metrics.GetStageExecutionDetailsRequest,
        dict,
    ],
)
def test_get_stage_execution_details(request_type, transport: str = "grpc"):
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_stage_execution_details), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = metrics.StageExecutionDetails(
            next_page_token="next_page_token_value",
        )
        response = client.get_stage_execution_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == metrics.GetStageExecutionDetailsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.GetStageExecutionDetailsPager)
    assert response.next_page_token == "next_page_token_value"


def test_get_stage_execution_details_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_stage_execution_details), "__call__"
    ) as call:
        client.get_stage_execution_details()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == metrics.GetStageExecutionDetailsRequest()


@pytest.mark.asyncio
async def test_get_stage_execution_details_async(
    transport: str = "grpc_asyncio",
    request_type=metrics.GetStageExecutionDetailsRequest,
):
    client = MetricsV1Beta3AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_stage_execution_details), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            metrics.StageExecutionDetails(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.get_stage_execution_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == metrics.GetStageExecutionDetailsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.GetStageExecutionDetailsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.asyncio
async def test_get_stage_execution_details_async_from_dict():
    await test_get_stage_execution_details_async(request_type=dict)


def test_get_stage_execution_details_pager(transport_name: str = "grpc"):
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_stage_execution_details), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            metrics.StageExecutionDetails(
                workers=[
                    metrics.WorkerDetails(),
                    metrics.WorkerDetails(),
                    metrics.WorkerDetails(),
                ],
                next_page_token="abc",
            ),
            metrics.StageExecutionDetails(
                workers=[],
                next_page_token="def",
            ),
            metrics.StageExecutionDetails(
                workers=[
                    metrics.WorkerDetails(),
                ],
                next_page_token="ghi",
            ),
            metrics.StageExecutionDetails(
                workers=[
                    metrics.WorkerDetails(),
                    metrics.WorkerDetails(),
                ],
            ),
            RuntimeError,
        )

        metadata = ()
        pager = client.get_stage_execution_details(request={})

        assert pager._metadata == metadata

        results = [i for i in pager]
        assert len(results) == 6
        assert all(isinstance(i, metrics.WorkerDetails) for i in results)


def test_get_stage_execution_details_pages(transport_name: str = "grpc"):
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_stage_execution_details), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            metrics.StageExecutionDetails(
                workers=[
                    metrics.WorkerDetails(),
                    metrics.WorkerDetails(),
                    metrics.WorkerDetails(),
                ],
                next_page_token="abc",
            ),
            metrics.StageExecutionDetails(
                workers=[],
                next_page_token="def",
            ),
            metrics.StageExecutionDetails(
                workers=[
                    metrics.WorkerDetails(),
                ],
                next_page_token="ghi",
            ),
            metrics.StageExecutionDetails(
                workers=[
                    metrics.WorkerDetails(),
                    metrics.WorkerDetails(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.get_stage_execution_details(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_get_stage_execution_details_async_pager():
    client = MetricsV1Beta3AsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_stage_execution_details),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            metrics.StageExecutionDetails(
                workers=[
                    metrics.WorkerDetails(),
                    metrics.WorkerDetails(),
                    metrics.WorkerDetails(),
                ],
                next_page_token="abc",
            ),
            metrics.StageExecutionDetails(
                workers=[],
                next_page_token="def",
            ),
            metrics.StageExecutionDetails(
                workers=[
                    metrics.WorkerDetails(),
                ],
                next_page_token="ghi",
            ),
            metrics.StageExecutionDetails(
                workers=[
                    metrics.WorkerDetails(),
                    metrics.WorkerDetails(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.get_stage_execution_details(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, metrics.WorkerDetails) for i in responses)


@pytest.mark.asyncio
async def test_get_stage_execution_details_async_pages():
    client = MetricsV1Beta3AsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_stage_execution_details),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            metrics.StageExecutionDetails(
                workers=[
                    metrics.WorkerDetails(),
                    metrics.WorkerDetails(),
                    metrics.WorkerDetails(),
                ],
                next_page_token="abc",
            ),
            metrics.StageExecutionDetails(
                workers=[],
                next_page_token="def",
            ),
            metrics.StageExecutionDetails(
                workers=[
                    metrics.WorkerDetails(),
                ],
                next_page_token="ghi",
            ),
            metrics.StageExecutionDetails(
                workers=[
                    metrics.WorkerDetails(),
                    metrics.WorkerDetails(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.get_stage_execution_details(request={})
        ).pages:  # pragma: no branch
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.MetricsV1Beta3GrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = MetricsV1Beta3Client(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.MetricsV1Beta3GrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = MetricsV1Beta3Client(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.MetricsV1Beta3GrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = MetricsV1Beta3Client(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = mock.Mock()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = MetricsV1Beta3Client(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.MetricsV1Beta3GrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = MetricsV1Beta3Client(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.MetricsV1Beta3GrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = MetricsV1Beta3Client(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.MetricsV1Beta3GrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.MetricsV1Beta3GrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.MetricsV1Beta3GrpcTransport,
        transports.MetricsV1Beta3GrpcAsyncIOTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.MetricsV1Beta3GrpcTransport,
    )


def test_metrics_v1_beta3_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.MetricsV1Beta3Transport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_metrics_v1_beta3_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.dataflow_v1beta3.services.metrics_v1_beta3.transports.MetricsV1Beta3Transport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.MetricsV1Beta3Transport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "get_job_metrics",
        "get_job_execution_details",
        "get_stage_execution_details",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()


def test_metrics_v1_beta3_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch(
        "google.cloud.dataflow_v1beta3.services.metrics_v1_beta3.transports.MetricsV1Beta3Transport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.MetricsV1Beta3Transport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/compute.readonly",
                "https://www.googleapis.com/auth/userinfo.email",
            ),
            quota_project_id="octopus",
        )


def test_metrics_v1_beta3_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch(
        "google.cloud.dataflow_v1beta3.services.metrics_v1_beta3.transports.MetricsV1Beta3Transport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.MetricsV1Beta3Transport()
        adc.assert_called_once()


def test_metrics_v1_beta3_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        MetricsV1Beta3Client()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/compute.readonly",
                "https://www.googleapis.com/auth/userinfo.email",
            ),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.MetricsV1Beta3GrpcTransport,
        transports.MetricsV1Beta3GrpcAsyncIOTransport,
    ],
)
def test_metrics_v1_beta3_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/compute.readonly",
                "https://www.googleapis.com/auth/userinfo.email",
            ),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.MetricsV1Beta3GrpcTransport, grpc_helpers),
        (transports.MetricsV1Beta3GrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_metrics_v1_beta3_transport_create_channel(transport_class, grpc_helpers):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel", autospec=True
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])

        create_channel.assert_called_with(
            "dataflow.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/compute.readonly",
                "https://www.googleapis.com/auth/userinfo.email",
            ),
            scopes=["1", "2"],
            default_host="dataflow.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.MetricsV1Beta3GrpcTransport,
        transports.MetricsV1Beta3GrpcAsyncIOTransport,
    ],
)
def test_metrics_v1_beta3_grpc_transport_client_cert_source_for_mtls(transport_class):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds,
        )
        mock_create_channel.assert_called_once_with(
            "squid.clam.whelk:443",
            credentials=cred,
            credentials_file=None,
            scopes=None,
            ssl_credentials=mock_ssl_channel_creds,
            quota_project_id=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )

    # Check if ssl_channel_credentials is not provided, then client_cert_source_for_mtls
    # is used.
    with mock.patch.object(transport_class, "create_channel", return_value=mock.Mock()):
        with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_cred:
            transport_class(
                credentials=cred,
                client_cert_source_for_mtls=client_cert_source_callback,
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert, private_key=expected_key
            )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
    ],
)
def test_metrics_v1_beta3_host_no_port(transport_name):
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="dataflow.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == ("dataflow.googleapis.com:443")


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
    ],
)
def test_metrics_v1_beta3_host_with_port(transport_name):
    client = MetricsV1Beta3Client(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="dataflow.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == ("dataflow.googleapis.com:8000")


def test_metrics_v1_beta3_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.MetricsV1Beta3GrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_metrics_v1_beta3_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.MetricsV1Beta3GrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize(
    "transport_class",
    [
        transports.MetricsV1Beta3GrpcTransport,
        transports.MetricsV1Beta3GrpcAsyncIOTransport,
    ],
)
def test_metrics_v1_beta3_transport_channel_mtls_with_client_cert_source(
    transport_class,
):
    with mock.patch(
        "grpc.ssl_channel_credentials", autospec=True
    ) as grpc_ssl_channel_cred:
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, "default") as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel
            assert transport._ssl_channel_credentials == mock_ssl_cred


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize(
    "transport_class",
    [
        transports.MetricsV1Beta3GrpcTransport,
        transports.MetricsV1Beta3GrpcAsyncIOTransport,
    ],
)
def test_metrics_v1_beta3_transport_channel_mtls_with_adc(transport_class):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = MetricsV1Beta3Client.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = MetricsV1Beta3Client.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = MetricsV1Beta3Client.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = MetricsV1Beta3Client.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = MetricsV1Beta3Client.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = MetricsV1Beta3Client.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = MetricsV1Beta3Client.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = MetricsV1Beta3Client.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = MetricsV1Beta3Client.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = MetricsV1Beta3Client.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = MetricsV1Beta3Client.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = MetricsV1Beta3Client.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = MetricsV1Beta3Client.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = MetricsV1Beta3Client.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = MetricsV1Beta3Client.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.MetricsV1Beta3Transport, "_prep_wrapped_messages"
    ) as prep:
        client = MetricsV1Beta3Client(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.MetricsV1Beta3Transport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = MetricsV1Beta3Client.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


@pytest.mark.asyncio
async def test_transport_close_async():
    client = MetricsV1Beta3AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc_asyncio",
    )
    with mock.patch.object(
        type(getattr(client.transport, "grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close():
    transports = {
        "grpc": "_grpc_channel",
    }

    for transport, close_name in transports.items():
        client = MetricsV1Beta3Client(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        with mock.patch.object(
            type(getattr(client.transport, close_name)), "close"
        ) as close:
            with client:
                close.assert_not_called()
            close.assert_called_once()


def test_client_ctx():
    transports = [
        "grpc",
    ]
    for transport in transports:
        client = MetricsV1Beta3Client(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()


@pytest.mark.parametrize(
    "client_class,transport_class",
    [
        (MetricsV1Beta3Client, transports.MetricsV1Beta3GrpcTransport),
        (MetricsV1Beta3AsyncClient, transports.MetricsV1Beta3GrpcAsyncIOTransport),
    ],
)
def test_api_key_credentials(client_class, transport_class):
    with mock.patch.object(
        google.auth._default, "get_api_key_credentials", create=True
    ) as get_api_key_credentials:
        mock_cred = mock.Mock()
        get_api_key_credentials.return_value = mock_cred
        options = client_options.ClientOptions()
        options.api_key = "api_key"
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options)
            patched.assert_called_once_with(
                credentials=mock_cred,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

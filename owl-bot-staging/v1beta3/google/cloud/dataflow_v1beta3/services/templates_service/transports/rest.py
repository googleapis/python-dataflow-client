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

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from google.protobuf import json_format
from requests import __version__ as requests_version
import dataclasses
import re
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.cloud.dataflow_v1beta3.types import jobs
from google.cloud.dataflow_v1beta3.types import templates

from .base import TemplatesServiceTransport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class TemplatesServiceRestInterceptor:
    """Interceptor for TemplatesService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TemplatesServiceRestTransport.

    .. code-block:: python
        class MyCustomTemplatesServiceInterceptor(TemplatesServiceRestInterceptor):
            def pre_create_job_from_template(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_job_from_template(response):
                logging.log(f"Received response: {response}")

            def pre_get_template(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_template(response):
                logging.log(f"Received response: {response}")

            def pre_launch_template(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_launch_template(response):
                logging.log(f"Received response: {response}")

        transport = TemplatesServiceRestTransport(interceptor=MyCustomTemplatesServiceInterceptor())
        client = TemplatesServiceClient(transport=transport)


    """
    def pre_create_job_from_template(self, request: templates.CreateJobFromTemplateRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[templates.CreateJobFromTemplateRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_job_from_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TemplatesService server.
        """
        return request, metadata

    def post_create_job_from_template(self, response: jobs.Job) -> jobs.Job:
        """Post-rpc interceptor for create_job_from_template

        Override in a subclass to manipulate the response
        after it is returned by the TemplatesService server but before
        it is returned to user code.
        """
        return response
    def pre_get_template(self, request: templates.GetTemplateRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[templates.GetTemplateRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TemplatesService server.
        """
        return request, metadata

    def post_get_template(self, response: templates.GetTemplateResponse) -> templates.GetTemplateResponse:
        """Post-rpc interceptor for get_template

        Override in a subclass to manipulate the response
        after it is returned by the TemplatesService server but before
        it is returned to user code.
        """
        return response
    def pre_launch_template(self, request: templates.LaunchTemplateRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[templates.LaunchTemplateRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for launch_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TemplatesService server.
        """
        return request, metadata

    def post_launch_template(self, response: templates.LaunchTemplateResponse) -> templates.LaunchTemplateResponse:
        """Post-rpc interceptor for launch_template

        Override in a subclass to manipulate the response
        after it is returned by the TemplatesService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class TemplatesServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: TemplatesServiceRestInterceptor


class TemplatesServiceRestTransport(TemplatesServiceTransport):
    """REST backend transport for TemplatesService.

    Provides a method to create Cloud Dataflow jobs from
    templates.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    NOTE: This REST transport functionality is currently in a beta
    state (preview). We welcome your feedback via an issue in this
    library's source repository. Thank you!
    """

    def __init__(self, *,
            host: str = 'dataflow.googleapis.com',
            credentials: ga_credentials.Credentials=None,
            credentials_file: str=None,
            scopes: Sequence[str]=None,
            client_cert_source_for_mtls: Callable[[
                ], Tuple[bytes, bytes]]=None,
            quota_project_id: Optional[str]=None,
            client_info: gapic_v1.client_info.ClientInfo=DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool]=False,
            url_scheme: str='https',
            interceptor: Optional[TemplatesServiceRestInterceptor] = None,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

       NOTE: This REST transport functionality is currently in a beta
       state (preview). We welcome your feedback via a GitHub issue in
       this library's repository. Thank you!

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(f"Unexpected hostname structure: {host}")  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or TemplatesServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateJobFromTemplate(TemplatesServiceRestStub):
        def __hash__(self):
            return hash("CreateJobFromTemplate")

        def __call__(self,
                request: templates.CreateJobFromTemplateRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: float=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> jobs.Job:
            r"""Call the create job from template method over HTTP.

            Args:
                request (~.templates.CreateJobFromTemplateRequest):
                    The request object. A request to create a Cloud Dataflow
                job from a template.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.jobs.Job:
                    Defines a job to be run by the Cloud
                Dataflow service.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1b3/projects/{project_id}/locations/{location}/templates',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v1b3/projects/{project_id}/templates',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_create_job_from_template(request, metadata)
            pb_request = templates.CreateJobFromTemplateRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = jobs.Job()
            pb_resp = jobs.Job.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_job_from_template(resp)
            return resp

    class _GetTemplate(TemplatesServiceRestStub):
        def __hash__(self):
            return hash("GetTemplate")

        def __call__(self,
                request: templates.GetTemplateRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: float=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> templates.GetTemplateResponse:
            r"""Call the get template method over HTTP.

            Args:
                request (~.templates.GetTemplateRequest):
                    The request object. A request to retrieve a Cloud
                Dataflow job template.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.templates.GetTemplateResponse:
                    The response to a GetTemplate
                request.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1b3/projects/{project_id}/locations/{location}/templates:get',
            },
{
                'method': 'get',
                'uri': '/v1b3/projects/{project_id}/templates:get',
            },
            ]
            request, metadata = self._interceptor.pre_get_template(request, metadata)
            pb_request = templates.GetTemplateRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = templates.GetTemplateResponse()
            pb_resp = templates.GetTemplateResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_template(resp)
            return resp

    class _LaunchTemplate(TemplatesServiceRestStub):
        def __hash__(self):
            return hash("LaunchTemplate")

        def __call__(self,
                request: templates.LaunchTemplateRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: float=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> templates.LaunchTemplateResponse:
            r"""Call the launch template method over HTTP.

            Args:
                request (~.templates.LaunchTemplateRequest):
                    The request object. A request to launch a template.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.templates.LaunchTemplateResponse:
                    Response to the request to launch a
                template.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1b3/projects/{project_id}/locations/{location}/templates:launch',
                'body': 'launch_parameters',
            },
{
                'method': 'post',
                'uri': '/v1b3/projects/{project_id}/templates:launch',
                'body': 'launch_parameters',
            },
            ]
            request, metadata = self._interceptor.pre_launch_template(request, metadata)
            pb_request = templates.LaunchTemplateRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = templates.LaunchTemplateResponse()
            pb_resp = templates.LaunchTemplateResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_launch_template(resp)
            return resp

    @property
    def create_job_from_template(self) -> Callable[
            [templates.CreateJobFromTemplateRequest],
            jobs.Job]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateJobFromTemplate(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_template(self) -> Callable[
            [templates.GetTemplateRequest],
            templates.GetTemplateResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTemplate(self._session, self._host, self._interceptor) # type: ignore

    @property
    def launch_template(self) -> Callable[
            [templates.LaunchTemplateRequest],
            templates.LaunchTemplateResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LaunchTemplate(self._session, self._host, self._interceptor) # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'TemplatesServiceRestTransport',
)
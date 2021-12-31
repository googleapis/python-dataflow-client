# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator

from google.cloud.dataflow_v1beta3.types import metrics


class GetJobExecutionDetailsPager:
    """A pager for iterating through ``get_job_execution_details`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataflow_v1beta3.types.JobExecutionDetails` object, and
    provides an ``__iter__`` method to iterate through its
    ``stages`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``GetJobExecutionDetails`` requests and continue to iterate
    through the ``stages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataflow_v1beta3.types.JobExecutionDetails`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., metrics.JobExecutionDetails],
            request: metrics.GetJobExecutionDetailsRequest,
            response: metrics.JobExecutionDetails,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataflow_v1beta3.types.GetJobExecutionDetailsRequest):
                The initial request object.
            response (google.cloud.dataflow_v1beta3.types.JobExecutionDetails):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = metrics.GetJobExecutionDetailsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[metrics.JobExecutionDetails]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[metrics.StageSummary]:
        for page in self.pages:
            yield from page.stages

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class GetJobExecutionDetailsAsyncPager:
    """A pager for iterating through ``get_job_execution_details`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataflow_v1beta3.types.JobExecutionDetails` object, and
    provides an ``__aiter__`` method to iterate through its
    ``stages`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``GetJobExecutionDetails`` requests and continue to iterate
    through the ``stages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataflow_v1beta3.types.JobExecutionDetails`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[metrics.JobExecutionDetails]],
            request: metrics.GetJobExecutionDetailsRequest,
            response: metrics.JobExecutionDetails,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataflow_v1beta3.types.GetJobExecutionDetailsRequest):
                The initial request object.
            response (google.cloud.dataflow_v1beta3.types.JobExecutionDetails):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = metrics.GetJobExecutionDetailsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[metrics.JobExecutionDetails]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[metrics.StageSummary]:
        async def async_generator():
            async for page in self.pages:
                for response in page.stages:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class GetStageExecutionDetailsPager:
    """A pager for iterating through ``get_stage_execution_details`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataflow_v1beta3.types.StageExecutionDetails` object, and
    provides an ``__iter__`` method to iterate through its
    ``workers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``GetStageExecutionDetails`` requests and continue to iterate
    through the ``workers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataflow_v1beta3.types.StageExecutionDetails`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., metrics.StageExecutionDetails],
            request: metrics.GetStageExecutionDetailsRequest,
            response: metrics.StageExecutionDetails,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataflow_v1beta3.types.GetStageExecutionDetailsRequest):
                The initial request object.
            response (google.cloud.dataflow_v1beta3.types.StageExecutionDetails):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = metrics.GetStageExecutionDetailsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[metrics.StageExecutionDetails]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[metrics.WorkerDetails]:
        for page in self.pages:
            yield from page.workers

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class GetStageExecutionDetailsAsyncPager:
    """A pager for iterating through ``get_stage_execution_details`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataflow_v1beta3.types.StageExecutionDetails` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``GetStageExecutionDetails`` requests and continue to iterate
    through the ``workers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataflow_v1beta3.types.StageExecutionDetails`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[metrics.StageExecutionDetails]],
            request: metrics.GetStageExecutionDetailsRequest,
            response: metrics.StageExecutionDetails,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataflow_v1beta3.types.GetStageExecutionDetailsRequest):
                The initial request object.
            response (google.cloud.dataflow_v1beta3.types.StageExecutionDetails):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = metrics.GetStageExecutionDetailsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[metrics.StageExecutionDetails]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[metrics.WorkerDetails]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)

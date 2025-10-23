# Copyright 2025-present Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from intx_sdk.client import Client
from intx_sdk.utils import append_query_param, append_pagination_params
from .get_index_candles import GetIndexCandlesRequest, GetIndexCandlesResponse
from .get_index_composition import GetIndexCompositionRequest, GetIndexCompositionResponse
from .get_index_composition_history import GetIndexCompositionHistoryRequest, GetIndexCompositionHistoryResponse
from .get_index_price import GetIndexPriceRequest, GetIndexPriceResponse


class IndexService:
    """Service for index-related operations."""

    def __init__(self, client: Client):
        """
        Initialize the IndexService.

        Args:
            client: The HTTP client for making API requests
        """
        self.client = client

    def get_index_candles(self, request: GetIndexCandlesRequest) -> GetIndexCandlesResponse:
        """
        Get candle data for an index.

        Args:
            request: GetIndexCandlesRequest with index, granularity, start, and optional end

        Returns:
            GetIndexCandlesResponse containing the candle data
        """
        path = f"/index/{request.index}/candles"

        query_params = append_query_param("", 'granularity', request.granularity)
        query_params = append_query_param(query_params, 'start', request.start)

        if request.end:
            query_params = append_query_param(query_params, 'end', request.end)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return GetIndexCandlesResponse(response=response.json())

    def get_index_composition(self, request: GetIndexCompositionRequest) -> GetIndexCompositionResponse:
        """
        Get the composition of an index.

        Args:
            request: GetIndexCompositionRequest with index

        Returns:
            GetIndexCompositionResponse containing the composition data
        """
        path = f"/index/{request.index}/composition"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetIndexCompositionResponse(response=response.json())

    def get_index_composition_history(self, request: GetIndexCompositionHistoryRequest) -> GetIndexCompositionHistoryResponse:
        """
        Get the composition history for an index.

        Args:
            request: GetIndexCompositionHistoryRequest with index, optional time_from, and pagination

        Returns:
            GetIndexCompositionHistoryResponse containing the composition history data
        """
        path = f"/index/{request.index}/composition-history"

        query_params = append_query_param("", 'time_from', request.time_from)
        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return GetIndexCompositionHistoryResponse(response=response.json())

    def get_index_price(self, request: GetIndexPriceRequest) -> GetIndexPriceResponse:
        """
        Get the current price of an index.

        Args:
            request: GetIndexPriceRequest with index

        Returns:
            GetIndexPriceResponse containing the price data
        """
        path = f"/index/{request.index}/price"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetIndexPriceResponse(response=response.json())

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
from intx_sdk.utils import append_query_param
from intx_sdk.services.model import Rankings, RankingStatistics, RankingStatistic
from .get_rankings import GetRankingsRequest, GetRankingsResponse


class RankingsService:
    """Service for rankings-related operations."""

    def __init__(self, client: Client):
        """
        Initialize the RankingsService.

        Args:
            client: The HTTP client for making API requests
        """
        self.client = client

    def get_rankings(self, request: GetRankingsRequest) -> GetRankingsResponse:
        """
        Get rankings statistics.

        Args:
            request: GetRankingsRequest with instrument type and optional filters

        Returns:
            GetRankingsResponse containing the rankings data
        """
        path = "/rankings/statistics"

        query_params = ""
        if request.instrument_type:
            query_params = append_query_param(query_params, 'instrument_type', request.instrument_type)
        if request.period:
            query_params = append_query_param(query_params, 'period', request.period)
        if request.instruments:
            query_params = append_query_param(query_params, 'instruments', request.instruments)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        maker = RankingStatistic(**data['statistics']['maker'])
        taker = RankingStatistic(**data['statistics']['taker'])
        total = RankingStatistic(**data['statistics']['total'])
        statistics = RankingStatistics(maker=maker, taker=taker, total=total)
        rankings = Rankings(last_updated=data['last_updated'], statistics=statistics)
        return GetRankingsResponse(rankings=rankings)

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
#  limitations under the License.

from dataclasses import dataclass
from typing import List, Optional
from intx_sdk.base_response import BaseResponse
from intx_sdk.client import Client
from intx_sdk.credentials import Credentials


@dataclass
class GetIndexPriceRequest:
    index: str
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class GetIndexPriceResponse(BaseResponse):
    request: GetIndexPriceRequest


class IntxClient:
    def __init__(self, credentials: Credentials, base_url: Optional[str] = None):
        self.client = Client(credentials, base_url=base_url)

    def get_index_price(self, request: GetIndexPriceRequest) -> GetIndexPriceResponse:
        path = f"/index/{request.index}/price"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetIndexPriceResponse(response.json(), request)

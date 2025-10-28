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

from dataclasses import dataclass, field
from typing import List, Optional
from intx_sdk.utils import PaginationParams
from intx_sdk.services.model import Order


@dataclass
class ListOpenOrdersRequest:
    portfolio: Optional[str] = None
    instrument: Optional[str] = None
    instrument_type: Optional[str] = None
    client_order_id: Optional[str] = None
    event_type: Optional[str] = None
    order_type: Optional[str] = None
    side: Optional[str] = None
    ref_datetime: Optional[str] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class ListOpenOrdersResponse:
    orders: List[Order] = field(default_factory=list)

    def __init__(self, **kwargs):
        # Handle paginated response with 'results' key
        orders_data = kwargs.get('results', kwargs.get('orders', []))
        self.orders = [Order(**order) if isinstance(order, dict) else order for order in orders_data]

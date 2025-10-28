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
from intx_sdk.services.model import Aggregation


@dataclass
class GetIndexCandlesRequest:
    index: str
    granularity: str
    start: str
    end: Optional[str] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class GetIndexCandlesResponse:
    aggregations: List[Aggregation] = field(default_factory=list)

    def __init__(self, **kwargs):
        aggregations_data = kwargs.get('aggregations', [])
        self.aggregations = [Aggregation(**agg) if isinstance(agg, dict) else agg for agg in aggregations_data]

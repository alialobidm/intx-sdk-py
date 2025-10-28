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
from intx_sdk.services.model import IndexComposition


@dataclass
class GetIndexCompositionHistoryRequest:
    index: str
    time_from: Optional[str] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class GetIndexCompositionHistoryResponse:
    compositions: List[IndexComposition] = field(default_factory=list)

    def __init__(self, **kwargs):
        compositions_data = kwargs.get('compositions', [])
        self.compositions = [IndexComposition(**comp) if isinstance(comp, dict) else comp for comp in compositions_data]

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
from intx_sdk.services.model import FeeTier


@dataclass
class ListFeeRateTiersRequest:
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class ListFeeRateTiersResponse:
    fee_tiers: List[FeeTier] = field(default_factory=list)

    def __init__(self, fee_tiers):
        self.fee_tiers = [FeeTier(**tier) if isinstance(tier, dict) else tier for tier in fee_tiers]

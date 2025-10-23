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

from dataclasses import dataclass
from typing import Optional


@dataclass
class Portfolio:
    portfolio_id: str
    portfolio_uuid: str
    name: str
    user_uuid: str
    maker_fee_rate: str
    taker_fee_rate: str
    trading_lock: bool
    withdrawal_lock: bool
    borrow_disabled: bool
    is_lsp: bool
    is_default: bool
    cross_collateral_enabled: bool
    auto_margin_enabled: bool
    pre_launch_trading_enabled: bool
    position_offsets_enabled: bool
    margin_call_enabled: bool = False
    close_only: bool = False
    forced_liquidation: bool = False
    disable_overdraft_protection: bool = False


@dataclass
class AddressBookEntry:
    recipient_type: str
    recipient_id: str
    label: str
    status: str
    asset: str
    network_arn_id: str
    created_at: str
    nick_name: Optional[str] = None


@dataclass
class Asset:
    asset_id: str
    asset_uuid: str
    asset_name: str
    status: str
    collateral_weight: str
    supported_networks_enabled: bool
    min_borrow_qty: str
    max_borrow_qty: str
    loan_collateral_requirement_multiplier: str
    ecosystem_collateral_limit_breached: bool
    loan_initial_margin: str
    max_loan_leverage: str


@dataclass
class SupportedNetwork:
    asset_id: str
    asset_uuid: str
    asset_name: str
    network_arn_id: str
    min_withdrawal_amt: str
    max_withdrawal_amt: str
    network_confirms: int
    processing_time: str
    is_default: bool
    network_name: str
    display_name: str

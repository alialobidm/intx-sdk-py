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
class AssetLoan:
    portfolio_id: str
    asset_id: str
    delta: float
    total: float
    asset_uuid: str
    portfolio_uuid: str


@dataclass
class AssetBalance:
    asset_id: str
    asset_name: str
    asset_uuid: str
    quantity: float
    hold: float
    hold_available_for_collateral: float
    transfer_hold: float
    collateral_value: float
    max_withdraw_amount: float
    loan: float
    loan_collateral_requirement: float
    pledged_collateral_quantity: float
    loan_initial_margin_contribution: float
    collateral_backed_overdraft_loan: float
    user_requested_loan: float
    unreconciled_amount: float
    max_undelegate_amount: float


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


@dataclass
class FeeTier:
    fee_tier_type: str
    instrument_type: str
    fee_tier_id: int
    fee_tier_name: str
    maker_fee_rate: float
    taker_fee_rate: float
    min_balance: float
    min_volume: float
    require_balance_and_volume: bool


@dataclass
class Aggregation:
    start: str
    open: str
    high: str
    low: str
    close: str
    volume: Optional[str] = None


@dataclass
class IndexConstituent:
    symbol: str
    name: str
    rank: int
    cap_factor: str
    amount: str
    market_cap: str
    index_market_cap: str
    weight: str
    running_weight: str


@dataclass
class IndexComposition:
    product_id: str
    divisor: float
    timestamp: str
    inception_timestamp: str
    last_rebalance: str
    constituents: list


@dataclass
class IndexPrice:
    product_id: str
    status: str
    timestamp: str
    price: str
    price_24hr_change: str


@dataclass
class Pagination:
    result_limit: int
    result_offset: int


@dataclass
class InstrumentVolume:
    symbol: str
    volume: str
    notional: str


@dataclass
class VolumeTotals:
    total_instruments_volume: str
    total_instruments_notional: str
    total_exchange_volume: str
    total_exchange_notional: str


@dataclass
class DailyVolume:
    timestamp: str
    instruments: list
    totals: dict


@dataclass
class FundingRate:
    instrument_id: str
    funding_rate: float
    mark_price: float
    event_time: str


@dataclass
class Quote:
    best_bid_price: float
    best_bid_size: float
    best_ask_price: float
    best_ask_size: float
    trade_price: float
    trade_qty: float
    index_price: float
    mark_price: float
    settlement_price: float
    limit_up: float
    limit_down: float
    predicted_funding: float
    timestamp: str


@dataclass
class InstrumentDetails:
    instrument_id: int
    instrument_uuid: str
    symbol: str
    type: str
    mode: str
    base_asset_id: int
    base_asset_uuid: str
    base_asset_name: str
    quote_asset_id: int
    quote_asset_uuid: str
    quote_asset_name: str
    base_increment: float
    quote_increment: float
    price_band_percent: float
    market_order_percent: float
    qty_24hr: float
    notional_24hr: float
    avg_daily_qty: float
    avg_daily_notional: float
    previous_day_qty: float
    open_interest: float
    position_limit_qty: str
    position_limit_adq_pct: float
    position_notional_limit: str
    open_interest_notional_limit: str
    replacement_cost: float
    base_imf: float
    default_imf: float
    min_notional_value: float
    funding_interval: int
    trading_state: str
    quote: dict
    base_asset_multiplier: int
    underlying_type: str
    rfq_maker_fee_rate: float


@dataclass
class Order:
    order_id: int
    client_order_id: str
    side: str
    instrument_id: int
    instrument_uuid: str
    symbol: str
    portfolio_id: int
    portfolio_uuid: str
    type: str
    size: float
    tif: str
    event_type: str
    event_time: str
    submit_time: str
    order_status: str
    leaves_qty: str
    exec_qty: str
    avg_price: str
    fee: str
    post_only: bool
    close_only: bool
    price: Optional[float] = None
    stop_price: Optional[float] = None
    stop_limit_price: Optional[float] = None
    expire_time: Optional[str] = None
    stp_mode: Optional[str] = None
    algo_strategy: Optional[str] = None
    text: Optional[str] = None


@dataclass
class LoanAvailability:
    available: str


@dataclass
class PortfolioLoan:
    portfolio_id: str
    asset_id: str
    asset_uuid: str
    asset: str
    total_loan: str
    collateral_backed_overdraft_loan: str
    user_requested_loan: str
    collateral_requirement: str
    initial_margin_contribution: str
    initial_margin_requirement: str
    current_interest_rate: str
    pending_interest_charge: str


@dataclass
class OpenPositionLimit:
    symbol: str
    instrument_id: str
    instrument_uuid: str
    open_position_notional_limit: str


@dataclass
class PortfolioSummary:
    collateral: str
    unrealized_pnl: str
    unrealized_pnl_percent: str
    position_notional: str
    open_position_notional: str
    pending_fees: str
    borrow: str
    accrued_interest: str
    rolling_debt: str
    balance: str
    buying_power: str
    portfolio_initial_margin: float
    portfolio_current_margin: float
    portfolio_maintenance_margin: float
    portfolio_close_out_margin: float
    in_liquidation: bool
    unrealized_pnl_notional: float
    portfolio_initial_margin_notional: float
    portfolio_maintenance_margin_notional: float
    portfolio_close_out_margin_notional: float
    margin_override: float
    lock_up_initial_margin: float
    loan_collateral_requirement: str
    position_offset_notional: float


@dataclass
class Position:
    id: str
    symbol: str
    instrument_id: str
    instrument_uuid: str
    vwap: str
    net_size: str
    buy_order_qty: str
    sell_order_qty: str
    instrument_type: str
    side: str
    total_entry_value: str
    updated_time: str
    unrealized_pnl: str
    unrealized_pnl_percent: str
    realized_pnl: str
    realized_pnl_percent: str


@dataclass
class PortfolioDetail:
    summary: PortfolioSummary
    balances: list
    positions: list


@dataclass
class PortfolioPosition:
    id: str
    symbol: str
    instrument_id: str
    instrument_uuid: str
    vwap: str
    net_size: str
    buy_order_size: str
    sell_order_size: str
    im_contribution: float
    unrealized_pnl: str
    mark_price: str
    entry_vwap: str
    index_price: str


@dataclass
class TotalOpenPositionLimit:
    total_open_position_notional_limit: str
    total_open_position_notional_limit_enforced: bool


@dataclass
class PortfolioFeeRate:
    instrument_type: str
    fee_tier_id: str
    is_vip_tier: bool
    fee_tier_name: str
    maker_fee_rate: str
    taker_fee_rate: str
    is_override: bool
    trailing_30day_volume: str
    trailing_24hr_usdc_balance: str


@dataclass
class PortfolioFillPaginationResult:
    result_limit: int
    result_offset: int
    ref_datetime: str


@dataclass
class PortfolioFill:
    portfolio_id: str
    portfolio_uuid: str
    fill_id: str
    symbol: str
    fill_price: str
    fill_qty: str
    side: str
    event_time: str
    order_id: Optional[str] = None
    client_order_id: Optional[str] = None
    instrument_id: Optional[str] = None
    instrument_uuid: Optional[str] = None
    fee: Optional[str] = None
    liquidity_indicator: Optional[str] = None


@dataclass
class PortfolioFillsResult:
    pagination: PortfolioFillPaginationResult
    results: list


@dataclass
class TransferResult:
    success: bool


@dataclass
class MarginOverrideResult:
    portfolio_id: str
    margin_override: float


@dataclass
class LoanPreview:
    initial_margin_contribution: str
    initial_margin_delta: str
    portfolio_initial_margin: str
    portfolio_initial_margin_notional: str
    loan_collateral_requirement: str
    loan_collateral_requirement_delta: str
    total_loan: str
    loan_delta: str
    max_available: str
    reject_details: str
    is_valid: bool


@dataclass
class PositionOffset:
    primary_instrument_id: str
    secondary_instrument_id: str
    offset: str


@dataclass
class RankingStatistic:
    rank: str
    relative_percent: str
    volume: str


@dataclass
class RankingStatistics:
    maker: RankingStatistic
    taker: RankingStatistic
    total: RankingStatistic


@dataclass
class Rankings:
    last_updated: str
    statistics: RankingStatistics


@dataclass
class CounterpartyIdResult:
    portfolio_uuid: str
    counterparty_id: str


@dataclass
class CryptoAddressResult:
    address: str
    network_arn_id: str
    destination_tag: Optional[str] = None


@dataclass
class CounterpartyWithdrawalLimit:
    max_ctn_withdraw_amount: str


@dataclass
class PortfolioInfo:
    id: str
    uuid: str
    name: str


@dataclass
class Transfer:
    transfer_uuid: str
    transfer_type: str
    amount: str
    asset: str
    status: str
    network_name: str
    created_at: str
    updated_at: str
    from_portfolio: Optional[PortfolioInfo] = None
    to_portfolio: Optional[PortfolioInfo] = None
    from_address: Optional[str] = None
    to_address: Optional[str] = None
    from_cb_account: Optional[str] = None
    to_cb_account: Optional[str] = None
    from_counterparty_id: Optional[str] = None
    to_counterparty_id: Optional[str] = None
    instrument_id: Optional[str] = None
    instrument_symbol: Optional[str] = None
    txn_hash: Optional[str] = None
    position_id: Optional[str] = None


@dataclass
class TransferPaginationResult:
    result_limit: int
    result_offset: int


@dataclass
class TransfersResult:
    pagination: TransferPaginationResult
    results: list


@dataclass
class CounterpartyValidation:
    counterparty_id: str
    valid: bool


@dataclass
class WithdrawToCounterpartyResult:
    idem: str
    portfolio_uuid: str
    source_counterparty_id: str
    target_counterparty_id: str
    asset: str
    amount: str


@dataclass
class WithdrawToCryptoResult:
    idem: str

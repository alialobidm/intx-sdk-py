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

from dataclasses import asdict
from intx_sdk.client import Client
from intx_sdk.utils import append_query_param, append_pagination_params
from intx_sdk.services.model import (
    Portfolio,
    AssetLoan,
    AssetBalance,
    LoanAvailability,
    PortfolioLoan,
    OpenPositionLimit,
    PortfolioSummary,
    PortfolioDetail,
    PortfolioPosition,
    TotalOpenPositionLimit,
    PortfolioFeeRate,
    PortfolioFillPaginationResult,
    PortfolioFillsResult,
    TransferResult,
    MarginOverrideResult,
    LoanPreview,
)
from .list_portfolios import ListPortfoliosRequest, ListPortfoliosResponse
from .acquire_or_repay_loan import AcquireOrRepayLoanRequest, AcquireOrRepayLoanResponse
from .create_portfolio import CreatePortfolioRequest, CreatePortfolioResponse
from .enable_disable_auto_margin import EnableDisableAutoMarginRequest, EnableDisableAutoMarginResponse
from .enable_disable_cross_collateral import EnableDisableCrossCollateralRequest, EnableDisableCrossCollateralResponse
from .get_balance_for_portfolio_asset import GetBalanceForPortfolioAssetRequest, GetBalanceForPortfolioAssetResponse
from .get_fund_transfer_limit import GetFundTransferLimitRequest, GetFundTransferLimitResponse
from .get_portfolio import GetPortfolioRequest, GetPortfolioResponse
from .get_portfolio_details import GetPortfolioDetailsRequest, GetPortfolioDetailsResponse
from .get_portfolio_summary import GetPortfolioSummaryRequest, GetPortfolioSummaryResponse
from .get_position_for_portfolio_instrument import GetPositionForPortfolioInstrumentRequest, GetPositionForPortfolioInstrumentResponse
from .list_portfolio_balances import ListPortfolioBalancesRequest, ListPortfolioBalancesResponse
from .list_portfolio_fills import ListPortfolioFillsRequest, ListPortfolioFillsResponse
from .list_portfolio_fee_rates import ListPortfolioFeeRatesRequest, ListPortfolioFeeRatesResponse
from .transfer_position import TransferPositionRequest, TransferPositionResponse
from .transfer_funds import TransferFundsRequest, TransferFundsResponse
from .set_margin_override import SetMarginOverrideRequest, SetMarginOverrideResponse
from .preview_loan_update import PreviewLoanUpdateRequest, PreviewLoanUpdateResponse
from .patch_portfolio import PatchPortfolioRequest, PatchPortfolioResponse
from .list_portfolio_positions import ListPortfolioPositionsRequest, ListPortfolioPositionsResponse
from .get_asset_loan_availability import GetAssetLoanAvailabilityRequest, GetAssetLoanAvailabilityResponse
from .get_loan_info_for_portfolio_asset import GetLoanInfoForPortfolioAssetRequest, GetLoanInfoForPortfolioAssetResponse
from .update_portfolio import UpdatePortfolioRequest, UpdatePortfolioResponse
from .list_open_position_limits_for_all_instruments import ListOpenPositionLimitsForAllInstrumentsRequest, ListOpenPositionLimitsForAllInstrumentsResponse
from .list_fills_by_portfolios import ListFillsByPortfoliosRequest, ListFillsByPortfoliosResponse
from .list_active_loans_for_portfolio import ListActiveLoansForPortfolioRequest, ListActiveLoansForPortfolioResponse
from .get_open_position_limits_for_portfolio_instrument import GetOpenPositionLimitsForPortfolioInstrumentRequest, GetOpenPositionLimitsForPortfolioInstrumentResponse
from .get_the_total_open_position_limit_for_portfolio import GetTheTotalOpenPositionLimitForPortfolioRequest, GetTheTotalOpenPositionLimitForPortfolioResponse


class PortfoliosService:
    def __init__(self, client: Client):
        self.client = client

    def list_portfolios(self, request: ListPortfoliosRequest) -> ListPortfoliosResponse:
        path = "/portfolios"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        portfolios_data = response.json()
        portfolios = [Portfolio(**portfolio) for portfolio in portfolios_data]
        return ListPortfoliosResponse(portfolios=portfolios)

    def create_portfolio(self, request: CreatePortfolioRequest) -> CreatePortfolioResponse:
        path = "/portfolios"
        body = {"name": request.name}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        portfolio = Portfolio(**data)
        return CreatePortfolioResponse(portfolio=portfolio)

    def acquire_or_repay_loan(self, request: AcquireOrRepayLoanRequest) -> AcquireOrRepayLoanResponse:
        path = f"/portfolios/{request.portfolio}/loans/{request.asset}"
        body = {k: v for k, v in asdict(request).items() if v is not None and k != 'allowed_status_codes'}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        loan = AssetLoan(**data)
        return AcquireOrRepayLoanResponse(loan=loan)

    def enable_disable_auto_margin(self, request: EnableDisableAutoMarginRequest) -> EnableDisableAutoMarginResponse:
        path = f"/portfolios/{request.portfolio}/auto-margin-enabled"
        body = {"enabled": request.enabled}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return EnableDisableAutoMarginResponse(response=response.json())

    def enable_disable_cross_collateral(self, request: EnableDisableCrossCollateralRequest) -> EnableDisableCrossCollateralResponse:
        path = f"/portfolios/{request.portfolio}/cross-collateral-enabled"
        body = {"enabled": request.enabled}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return EnableDisableCrossCollateralResponse(response=response.json())

    def get_balance_for_portfolio_asset(self, request: GetBalanceForPortfolioAssetRequest) -> GetBalanceForPortfolioAssetResponse:
        path = f"/portfolios/{request.portfolio}/balances/{request.asset}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        balance = AssetBalance(**data)
        return GetBalanceForPortfolioAssetResponse(balance=balance)

    def get_fund_transfer_limit(self, request: GetFundTransferLimitRequest) -> GetFundTransferLimitResponse:
        path = f"/portfolios/transfer/{request.portfolio}/{request.asset}/transfer-limit"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        return GetFundTransferLimitResponse(max_portfolio_transfer_amount=data["max_portfolio_transfer_amount"])

    def get_portfolio(self, request: GetPortfolioRequest) -> GetPortfolioResponse:
        path = f"/portfolios/{request.portfolio}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        portfolio = Portfolio(**data)
        return GetPortfolioResponse(portfolio=portfolio)

    def get_portfolio_details(self, request: GetPortfolioDetailsRequest) -> GetPortfolioDetailsResponse:
        path = f"/portfolios/{request.portfolio}/detail"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        summary = PortfolioSummary(**data['summary'])
        detail = PortfolioDetail(
            summary=summary,
            balances=data.get('balances', []),
            positions=data.get('positions', [])
        )
        return GetPortfolioDetailsResponse(portfolio_detail=detail)

    def get_portfolio_summary(self, request: GetPortfolioSummaryRequest) -> GetPortfolioSummaryResponse:
        path = f"/portfolios/{request.portfolio}/summary"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        summary = PortfolioSummary(**data)
        return GetPortfolioSummaryResponse(portfolio_summary=summary)

    def get_position_for_portfolio_instrument(self, request: GetPositionForPortfolioInstrumentRequest) -> GetPositionForPortfolioInstrumentResponse:
        path = f"/portfolios/{request.portfolio}/positions/{request.instrument}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        position = PortfolioPosition(**data)
        return GetPositionForPortfolioInstrumentResponse(position=position)

    def list_portfolio_balances(self, request: ListPortfolioBalancesRequest) -> ListPortfolioBalancesResponse:
        path = f"/portfolios/{request.portfolio}/balances"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        balances = [AssetBalance(**balance) for balance in data]
        return ListPortfolioBalancesResponse(balances=balances)

    def list_portfolio_fills(self, request: ListPortfolioFillsRequest) -> ListPortfolioFillsResponse:
        path = f"/portfolios/{request.portfolio}/fills"

        query_params = append_pagination_params("", request.pagination)
        query_params = append_query_param(query_params, 'portfolio', request.portfolio)
        query_params = append_query_param(query_params, 'order_id', request.order_id)
        query_params = append_query_param(query_params, 'client_order_id', request.client_order_id)
        query_params = append_query_param(query_params, 'ref_datetime', request.ref_datetime)
        query_params = append_query_param(query_params, 'time_from', request.time_from)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        pagination = PortfolioFillPaginationResult(**data['pagination'])
        fills_result = PortfolioFillsResult(pagination=pagination, results=data.get('results', []))
        return ListPortfolioFillsResponse(fills_result=fills_result)

    def list_portfolio_fee_rates(self, request: ListPortfolioFeeRatesRequest) -> ListPortfolioFeeRatesResponse:
        path = "/portfolios/fee-rates"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        fee_rates = [PortfolioFeeRate(**rate) for rate in data]
        return ListPortfolioFeeRatesResponse(fee_rates=fee_rates)

    def transfer_position(self, request: TransferPositionRequest) -> TransferPositionResponse:
        path = "/portfolios/transfer-position"
        body = {
            "from": request.from_portfolio,
            "to": request.to_portfolio,
            "instrument": request.instrument,
            "quantity": request.quantity,
            "side": request.side
        }
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        transfer_result = TransferResult(**data)
        return TransferPositionResponse(transfer_result=transfer_result)

    def transfer_funds(self, request: TransferFundsRequest) -> TransferFundsResponse:
        path = "/portfolios/transfer"
        body = {
            "from": request.from_portfolio,
            "to": request.to_portfolio,
            "asset": request.asset,
            "amount": request.amount
        }
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        transfer_result = TransferResult(**data)
        return TransferFundsResponse(transfer_result=transfer_result)

    def set_margin_override(self, request: SetMarginOverrideRequest) -> SetMarginOverrideResponse:
        path = "/portfolios/margin"
        body = {k: v for k, v in asdict(request).items() if v is not None and k != 'allowed_status_codes'}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        margin_override_result = MarginOverrideResult(**data)
        return SetMarginOverrideResponse(margin_override_result=margin_override_result)

    def preview_loan_update(self, request: PreviewLoanUpdateRequest) -> PreviewLoanUpdateResponse:
        path = f"/portfolios/{request.portfolio}/loans/{request.asset}/preview"
        body = {k: v for k, v in asdict(request).items() if v is not None and k not in ['portfolio', 'asset', 'allowed_status_codes']}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        loan_preview = LoanPreview(**data)
        return PreviewLoanUpdateResponse(loan_preview=loan_preview)

    def patch_portfolio(self, request: PatchPortfolioRequest) -> PatchPortfolioResponse:
        path = f"/portfolios/{request.portfolio}"
        body = {k: v for k, v in asdict(request).items() if v is not None and k not in ['portfolio', 'portfolio_name', 'allowed_status_codes']}
        response = self.client.request("PATCH", path, body=body, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        portfolio = Portfolio(**data)
        return PatchPortfolioResponse(portfolio=portfolio)

    def list_portfolio_positions(self, request: ListPortfolioPositionsRequest) -> ListPortfolioPositionsResponse:
        path = f"/portfolios/{request.portfolio}/positions"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        positions = [PortfolioPosition(**position) for position in data]
        return ListPortfolioPositionsResponse(positions=positions)

    def get_asset_loan_availability(self, request: GetAssetLoanAvailabilityRequest) -> GetAssetLoanAvailabilityResponse:
        path = f"/portfolios/{request.portfolio}/loans/{request.asset}/availability"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        loan_availability = LoanAvailability(**data)
        return GetAssetLoanAvailabilityResponse(loan_availability=loan_availability)

    def get_loan_info_for_portfolio_asset(self, request: GetLoanInfoForPortfolioAssetRequest) -> GetLoanInfoForPortfolioAssetResponse:
        path = f"/portfolios/{request.portfolio}/loans/{request.asset}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        portfolio_loan = PortfolioLoan(**data)
        return GetLoanInfoForPortfolioAssetResponse(portfolio_loan=portfolio_loan)

    def update_portfolio(self, request: UpdatePortfolioRequest) -> UpdatePortfolioResponse:
        path = f"/portfolios/{request.portfolio}"
        body = {"name": request.name}
        response = self.client.request("PUT", path, body=body, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        portfolio = Portfolio(**data)
        return UpdatePortfolioResponse(portfolio=portfolio)

    def list_open_position_limits_for_all_instruments(self, request: ListOpenPositionLimitsForAllInstrumentsRequest) -> ListOpenPositionLimitsForAllInstrumentsResponse:
        path = f"/portfolios/{request.portfolio}/position-limits/positions"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        position_limits = [OpenPositionLimit(**limit) for limit in data]
        return ListOpenPositionLimitsForAllInstrumentsResponse(position_limits=position_limits)

    def list_fills_by_portfolios(self, request: ListFillsByPortfoliosRequest) -> ListFillsByPortfoliosResponse:
        path = "/portfolios/fills"
        query_params = append_pagination_params("", request.pagination)
        query_params = append_query_param(query_params, 'portfolios', request.portfolios)
        query_params = append_query_param(query_params, 'order_id', request.order_id)
        query_params = append_query_param(query_params, 'client_order_id', request.client_order_id)
        query_params = append_query_param(query_params, 'ref_datetime', request.ref_datetime)
        query_params = append_query_param(query_params, 'time_from', request.time_from)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        pagination = PortfolioFillPaginationResult(**data['pagination'])
        fills_result = PortfolioFillsResult(pagination=pagination, results=data.get('results', []))
        return ListFillsByPortfoliosResponse(fills_result=fills_result)

    def list_active_loans_for_portfolio(self, request: ListActiveLoansForPortfolioRequest) -> ListActiveLoansForPortfolioResponse:
        path = f"/portfolios/{request.portfolio}/loans"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        loans = [PortfolioLoan(**loan) for loan in data]
        return ListActiveLoansForPortfolioResponse(loans=loans)

    def get_open_position_limits_for_portfolio_instrument(self, request: GetOpenPositionLimitsForPortfolioInstrumentRequest) -> GetOpenPositionLimitsForPortfolioInstrumentResponse:
        path = f"/portfolios/{request.portfolio}/position-limits/positions/{request.instrument}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        open_position_limit = OpenPositionLimit(**data)
        return GetOpenPositionLimitsForPortfolioInstrumentResponse(open_position_limit=open_position_limit)

    def get_the_total_open_position_limit_for_portfolio(self, request: GetTheTotalOpenPositionLimitForPortfolioRequest) -> GetTheTotalOpenPositionLimitForPortfolioResponse:
        path = f"/portfolios/{request.portfolio}/position-limits"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        data = response.json()
        total_limit = TotalOpenPositionLimit(**data)
        return GetTheTotalOpenPositionLimitForPortfolioResponse(total_open_position_limit=total_limit)

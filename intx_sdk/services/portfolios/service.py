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
from intx_sdk.services.model import Portfolio
from .list_portfolios import ListPortfoliosRequest, ListPortfoliosResponse
from .acquire_or_repay_loan import AcquireOrRepayLoanRequest, AcquireOrRepayLoanResponse
from .create_portfolio import CreatePortfolioRequest, CreatePortfolioResponse
from .enable_disable_auto_margin import EnableDisableAutoMarginRequest, EnableDisableAutoMarginResponse
from .enable_disable_cross_collateral import EnableDisableCrossCollateralRequest, EnableDisableCrossCollateralResponse
from .get_balance_for_portfolio_asset import GetBalanceForPortfolioAssetRequest, GetBalanceForPortfolioAssetResponse
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
    """Service for portfolio-related operations."""

    def __init__(self, client: Client):
        """
        Initialize the PortfoliosService.

        Args:
            client: The HTTP client for making API requests
        """
        self.client = client

    def list_portfolios(self, request: ListPortfoliosRequest) -> ListPortfoliosResponse:
        """
        List all portfolios.

        Args:
            request: ListPortfoliosRequest with optional allowed_status_codes

        Returns:
            ListPortfoliosResponse containing the portfolio data
        """
        path = "/portfolios"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        portfolios_data = response.json()
        portfolios = [Portfolio(**portfolio) for portfolio in portfolios_data]
        return ListPortfoliosResponse(portfolios=portfolios)

    def create_portfolio(self, request: CreatePortfolioRequest) -> CreatePortfolioResponse:
        """
        Create a new portfolio.

        Args:
            request: CreatePortfolioRequest with portfolio name

        Returns:
            CreatePortfolioResponse containing the created portfolio data
        """
        path = "/portfolios"
        body = {"name": request.name}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreatePortfolioResponse(response=response.json())

    def acquire_or_repay_loan(self, request: AcquireOrRepayLoanRequest) -> AcquireOrRepayLoanResponse:
        """
        Acquire or repay a loan for a portfolio asset.

        Args:
            request: AcquireOrRepayLoanRequest with portfolio, asset, action, and amount

        Returns:
            AcquireOrRepayLoanResponse containing the loan operation result
        """
        path = f"/portfolios/{request.portfolio}/loans/{request.asset}"
        body = {k: v for k, v in asdict(request).items() if v is not None and k != 'allowed_status_codes'}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return AcquireOrRepayLoanResponse(response=response.json())

    def enable_disable_auto_margin(self, request: EnableDisableAutoMarginRequest) -> EnableDisableAutoMarginResponse:
        """
        Enable or disable auto margin for a portfolio.

        Args:
            request: EnableDisableAutoMarginRequest with portfolio and enabled flag

        Returns:
            EnableDisableAutoMarginResponse containing the operation result
        """
        path = f"/portfolios/{request.portfolio}/auto-margin-enabled"
        body = {"enabled": request.enabled}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return EnableDisableAutoMarginResponse(response=response.json())

    def enable_disable_cross_collateral(self, request: EnableDisableCrossCollateralRequest) -> EnableDisableCrossCollateralResponse:
        """
        Enable or disable cross collateral for a portfolio.

        Args:
            request: EnableDisableCrossCollateralRequest with portfolio and enabled flag

        Returns:
            EnableDisableCrossCollateralResponse containing the operation result
        """
        path = f"/portfolios/{request.portfolio}/cross-collateral-enabled"
        body = {"enabled": request.enabled}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return EnableDisableCrossCollateralResponse(response=response.json())

    def get_balance_for_portfolio_asset(self, request: GetBalanceForPortfolioAssetRequest) -> GetBalanceForPortfolioAssetResponse:
        """
        Get balance for a specific asset in a portfolio.

        Args:
            request: GetBalanceForPortfolioAssetRequest with portfolio and asset

        Returns:
            GetBalanceForPortfolioAssetResponse containing the balance data
        """
        path = f"/portfolios/{request.portfolio}/balances/{request.asset}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetBalanceForPortfolioAssetResponse(response=response.json())

    def get_portfolio(self, request: GetPortfolioRequest) -> GetPortfolioResponse:
        """
        Get details for a specific portfolio.

        Args:
            request: GetPortfolioRequest with portfolio

        Returns:
            GetPortfolioResponse containing the portfolio data
        """
        path = f"/portfolios/{request.portfolio}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetPortfolioResponse(response=response.json())

    def get_portfolio_details(self, request: GetPortfolioDetailsRequest) -> GetPortfolioDetailsResponse:
        """
        Get detailed information for a portfolio.

        Args:
            request: GetPortfolioDetailsRequest with portfolio

        Returns:
            GetPortfolioDetailsResponse containing the detailed portfolio data
        """
        path = f"/portfolios/{request.portfolio}/detail"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetPortfolioDetailsResponse(response=response.json())

    def get_portfolio_summary(self, request: GetPortfolioSummaryRequest) -> GetPortfolioSummaryResponse:
        """
        Get summary information for a portfolio.

        Args:
            request: GetPortfolioSummaryRequest with portfolio

        Returns:
            GetPortfolioSummaryResponse containing the portfolio summary data
        """
        path = f"/portfolios/{request.portfolio}/summary"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetPortfolioSummaryResponse(response=response.json())

    def get_position_for_portfolio_instrument(self, request: GetPositionForPortfolioInstrumentRequest) -> GetPositionForPortfolioInstrumentResponse:
        """
        Get position for a specific instrument in a portfolio.

        Args:
            request: GetPositionForPortfolioInstrumentRequest with portfolio and instrument

        Returns:
            GetPositionForPortfolioInstrumentResponse containing the position data
        """
        path = f"/portfolios/{request.portfolio}/positions/{request.instrument}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetPositionForPortfolioInstrumentResponse(response=response.json())

    def list_portfolio_balances(self, request: ListPortfolioBalancesRequest) -> ListPortfolioBalancesResponse:
        """
        List all balances for a portfolio.

        Args:
            request: ListPortfolioBalancesRequest with portfolio

        Returns:
            ListPortfolioBalancesResponse containing the balances data
        """
        path = f"/portfolios/{request.portfolio}/balances"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return ListPortfolioBalancesResponse(response=response.json())

    def list_portfolio_fills(self, request: ListPortfolioFillsRequest) -> ListPortfolioFillsResponse:
        """
        List fills for a portfolio.

        Args:
            request: ListPortfolioFillsRequest with portfolio, optional pagination and filters

        Returns:
            ListPortfolioFillsResponse containing the fills data
        """
        path = f"/portfolios/{request.portfolio}/fills"

        query_params = append_pagination_params("", request.pagination)
        query_params = append_query_param(query_params, 'portfolio', request.portfolio)
        query_params = append_query_param(query_params, 'order_id', request.order_id)
        query_params = append_query_param(query_params, 'client_order_id', request.client_order_id)
        query_params = append_query_param(query_params, 'ref_datetime', request.ref_datetime)
        query_params = append_query_param(query_params, 'time_from', request.time_from)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListPortfolioFillsResponse(response=response.json())

    def list_portfolio_fee_rates(self, request: ListPortfolioFeeRatesRequest) -> ListPortfolioFeeRatesResponse:
        """
        List fee rates for portfolios.

        Args:
            request: ListPortfolioFeeRatesRequest with optional allowed_status_codes

        Returns:
            ListPortfolioFeeRatesResponse containing the fee rates data
        """
        path = "/portfolios/fee-rates"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return ListPortfolioFeeRatesResponse(response=response.json())

    def transfer_position(self, request: TransferPositionRequest) -> TransferPositionResponse:
        """
        Transfer a position between portfolios.

        Args:
            request: TransferPositionRequest with from_portfolio, to_portfolio, instrument, quantity, and side

        Returns:
            TransferPositionResponse containing the transfer result
        """
        path = "/portfolios/transfer-position"
        body = {
            "from": request.from_portfolio,
            "to": request.to_portfolio,
            "instrument": request.instrument,
            "quantity": request.quantity,
            "side": request.side
        }
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return TransferPositionResponse(response=response.json())

    def transfer_funds(self, request: TransferFundsRequest) -> TransferFundsResponse:
        """
        Transfer funds between portfolios.

        Args:
            request: TransferFundsRequest with from_portfolio, to_portfolio, asset, and amount

        Returns:
            TransferFundsResponse containing the transfer result
        """
        path = "/portfolios/transfer"
        body = {
            "from": request.from_portfolio,
            "to": request.to_portfolio,
            "asset": request.asset,
            "amount": request.amount
        }
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return TransferFundsResponse(response=response.json())

    def set_margin_override(self, request: SetMarginOverrideRequest) -> SetMarginOverrideResponse:
        """
        Set margin override for a portfolio.

        Args:
            request: SetMarginOverrideRequest with portfolio_id and margin_override

        Returns:
            SetMarginOverrideResponse containing the operation result
        """
        path = "/portfolios/margin"
        body = {k: v for k, v in asdict(request).items() if v is not None and k != 'allowed_status_codes'}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return SetMarginOverrideResponse(response=response.json())

    def preview_loan_update(self, request: PreviewLoanUpdateRequest) -> PreviewLoanUpdateResponse:
        """
        Preview a loan update for a portfolio asset.

        Args:
            request: PreviewLoanUpdateRequest with portfolio, asset, action, and amount

        Returns:
            PreviewLoanUpdateResponse containing the preview data
        """
        path = f"/portfolios/{request.portfolio}/loans/{request.asset}/preview"
        body = {k: v for k, v in asdict(request).items() if v is not None and k not in ['portfolio', 'asset', 'allowed_status_codes']}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return PreviewLoanUpdateResponse(response=response.json())

    def patch_portfolio(self, request: PatchPortfolioRequest) -> PatchPortfolioResponse:
        """
        Patch (update) a portfolio's settings.

        Args:
            request: PatchPortfolioRequest with portfolio and optional settings

        Returns:
            PatchPortfolioResponse containing the updated portfolio data
        """
        path = f"/portfolios/{request.portfolio}"
        body = {k: v for k, v in asdict(request).items() if v is not None and k not in ['portfolio', 'portfolio_name', 'allowed_status_codes']}
        response = self.client.request("PATCH", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return PatchPortfolioResponse(response=response.json())

    def list_portfolio_positions(self, request: ListPortfolioPositionsRequest) -> ListPortfolioPositionsResponse:
        """
        List all positions for a portfolio.

        Args:
            request: ListPortfolioPositionsRequest with portfolio

        Returns:
            ListPortfolioPositionsResponse containing the positions data
        """
        path = f"/portfolios/{request.portfolio}/positions"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return ListPortfolioPositionsResponse(response=response.json())

    def get_asset_loan_availability(self, request: GetAssetLoanAvailabilityRequest) -> GetAssetLoanAvailabilityResponse:
        """
        Get loan availability for a portfolio asset.

        Args:
            request: GetAssetLoanAvailabilityRequest with portfolio and asset

        Returns:
            GetAssetLoanAvailabilityResponse containing the loan availability data
        """
        path = f"/portfolios/{request.portfolio}/loans/{request.asset}/availability"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetAssetLoanAvailabilityResponse(response=response.json())

    def get_loan_info_for_portfolio_asset(self, request: GetLoanInfoForPortfolioAssetRequest) -> GetLoanInfoForPortfolioAssetResponse:
        """
        Get loan information for a portfolio asset.

        Args:
            request: GetLoanInfoForPortfolioAssetRequest with portfolio and asset

        Returns:
            GetLoanInfoForPortfolioAssetResponse containing the loan information
        """
        path = f"/portfolios/{request.portfolio}/loans/{request.asset}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetLoanInfoForPortfolioAssetResponse(response=response.json())

    def update_portfolio(self, request: UpdatePortfolioRequest) -> UpdatePortfolioResponse:
        """
        Update a portfolio's name.

        Args:
            request: UpdatePortfolioRequest with portfolio and name

        Returns:
            UpdatePortfolioResponse containing the updated portfolio data
        """
        path = f"/portfolios/{request.portfolio}"
        body = {"name": request.name}
        response = self.client.request("PUT", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return UpdatePortfolioResponse(response=response.json())

    def list_open_position_limits_for_all_instruments(self, request: ListOpenPositionLimitsForAllInstrumentsRequest) -> ListOpenPositionLimitsForAllInstrumentsResponse:
        """
        List open position limits for all instruments in a portfolio.

        Args:
            request: ListOpenPositionLimitsForAllInstrumentsRequest with portfolio

        Returns:
            ListOpenPositionLimitsForAllInstrumentsResponse containing the position limits data
        """
        path = f"/portfolios/{request.portfolio}/position-limits/positions"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return ListOpenPositionLimitsForAllInstrumentsResponse(response=response.json())

    def list_fills_by_portfolios(self, request: ListFillsByPortfoliosRequest) -> ListFillsByPortfoliosResponse:
        """
        List fills for multiple portfolios.

        Args:
            request: ListFillsByPortfoliosRequest with optional filters and pagination

        Returns:
            ListFillsByPortfoliosResponse containing the fills data
        """
        path = "/portfolios/fills"
        query_params = append_pagination_params("", request.pagination)
        query_params = append_query_param(query_params, 'portfolios', request.portfolios)
        query_params = append_query_param(query_params, 'order_id', request.order_id)
        query_params = append_query_param(query_params, 'client_order_id', request.client_order_id)
        query_params = append_query_param(query_params, 'ref_datetime', request.ref_datetime)
        query_params = append_query_param(query_params, 'time_from', request.time_from)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListFillsByPortfoliosResponse(response=response.json())

    def list_active_loans_for_portfolio(self, request: ListActiveLoansForPortfolioRequest) -> ListActiveLoansForPortfolioResponse:
        """
        List active loans for a portfolio.

        Args:
            request: ListActiveLoansForPortfolioRequest with portfolio

        Returns:
            ListActiveLoansForPortfolioResponse containing the active loans data
        """
        path = f"/portfolios/{request.portfolio}/loans"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return ListActiveLoansForPortfolioResponse(response=response.json())

    def get_open_position_limits_for_portfolio_instrument(self, request: GetOpenPositionLimitsForPortfolioInstrumentRequest) -> GetOpenPositionLimitsForPortfolioInstrumentResponse:
        """
        Get open position limits for a specific instrument in a portfolio.

        Args:
            request: GetOpenPositionLimitsForPortfolioInstrumentRequest with portfolio and instrument

        Returns:
            GetOpenPositionLimitsForPortfolioInstrumentResponse containing the position limits data
        """
        path = f"/portfolios/{request.portfolio}/position-limits/positions/{request.instrument}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetOpenPositionLimitsForPortfolioInstrumentResponse(response=response.json())

    def get_the_total_open_position_limit_for_portfolio(self, request: GetTheTotalOpenPositionLimitForPortfolioRequest) -> GetTheTotalOpenPositionLimitForPortfolioResponse:
        """
        Get the total open position limit for a portfolio.

        Args:
            request: GetTheTotalOpenPositionLimitForPortfolioRequest with portfolio

        Returns:
            GetTheTotalOpenPositionLimitForPortfolioResponse containing the total position limit data
        """
        path = f"/portfolios/{request.portfolio}/position-limits"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetTheTotalOpenPositionLimitForPortfolioResponse(response=response.json())

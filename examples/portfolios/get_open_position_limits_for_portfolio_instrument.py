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
import argparse
import os
from intx_sdk import IntxServicesClient
from intx_sdk.services.portfolios import GetOpenPositionLimitsForPortfolioInstrumentRequest


def main():
    parser = argparse.ArgumentParser(description="Get open position limits for portfolio instrument")
    parser.add_argument("--portfolio", default=os.getenv('INTX_PORTFOLIO_ID'), help="Portfolio ID (defaults to INTX_PORTFOLIO_ID env var)")
    parser.add_argument("--instrument", required=True, help="Instrument symbol")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = GetOpenPositionLimitsForPortfolioInstrumentRequest(
        portfolio=args.portfolio,
        instrument=args.instrument
    )

    try:
        response = client.portfolios.get_open_position_limits_for_portfolio_instrument(request)
        print(response)
    except Exception as e:
        print(f"failed to get open position limits for portfolio instrument: {e}")


if __name__ == "__main__":
    main()

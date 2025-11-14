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
from intx_sdk.services.portfolios import PatchPortfolioRequest


def main():
    parser = argparse.ArgumentParser(description="Patch portfolio settings")
    parser.add_argument("--portfolio", default=os.getenv('INTX_PORTFOLIO_ID'), help="Portfolio ID (defaults to INTX_PORTFOLIO_ID env var)")
    parser.add_argument("--portfolio-name", required=True, help="Portfolio name")
    parser.add_argument("--auto-margin-enabled", help="Auto margin enabled (optional)")
    parser.add_argument("--cross-collateral-enabled", help="Cross collateral enabled (optional)")
    parser.add_argument("--position-offsets-enabled", help="Position offsets enabled (optional)")
    parser.add_argument("--pre-launch-trading-enabled", help="Pre-launch trading enabled (optional)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = PatchPortfolioRequest(
        portfolio=args.portfolio,
        portfolio_name=args.portfolio_name,
        auto_margin_enabled=args.auto_margin_enabled,
        cross_collateral_enabled=args.cross_collateral_enabled,
        position_offsets_enabled=args.position_offsets_enabled,
        pre_launch_trading_enabled=args.pre_launch_trading_enabled
    )

    try:
        response = client.portfolios.patch_portfolio(request)
        print(response)
    except Exception as e:
        print(f"failed to patch portfolio: {e}")


if __name__ == "__main__":
    main()

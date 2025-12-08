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
from intx_sdk.services.portfolios import GetBalanceForPortfolioAssetRequest


def main():
    parser = argparse.ArgumentParser(
        description="Get balance for portfolio asset",
        epilog="""
Examples:
  # Get USDC balance
  python examples/portfolios/get_balance_for_portfolio_asset.py --asset USDC
"""
    )
    parser.add_argument("--asset", required=True, help="Asset symbol (e.g., USDC, BTC)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = GetBalanceForPortfolioAssetRequest(
        portfolio=os.getenv('INTX_PORTFOLIO_ID'),
        asset=args.asset
    )

    try:
        response = client.portfolios.get_balance_for_portfolio_asset(request)
        print(response)
    except Exception as e:
        print(f"failed to get balance for portfolio asset: {e}")


if __name__ == "__main__":
    main()

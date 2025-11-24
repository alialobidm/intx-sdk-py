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
from intx_sdk.services.portfolios import UpdatePortfolioRequest


def main():
    parser = argparse.ArgumentParser(
        description="Update portfolio",
        epilog="""
Examples:
  # Update portfolio name
  python examples/portfolios/update_portfolio.py --name "New Portfolio Name"
"""
    )
    parser.add_argument("--name", required=True, help="New portfolio name")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = UpdatePortfolioRequest(
        portfolio=os.getenv('INTX_PORTFOLIO_ID'),
        name=args.name
    )

    try:
        response = client.portfolios.update_portfolio(request)
        print(response)
    except Exception as e:
        print(f"failed to update portfolio: {e}")


if __name__ == "__main__":
    main()

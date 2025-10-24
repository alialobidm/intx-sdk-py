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
from intx_sdk import IntxServicesClient
from intx_sdk.services.portfolios import ListPortfolioFillsRequest


def main():
    parser = argparse.ArgumentParser(description="List portfolio fills")
    parser.add_argument("--portfolio", required=True, help="Portfolio ID")
    parser.add_argument("--order-id", help="Filter by order ID (optional)")
    parser.add_argument("--client-order-id", help="Filter by client order ID (optional)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env("INTX_CREDENTIALS")

    request = ListPortfolioFillsRequest(
        portfolio=args.portfolio,
        order_id=args.order_id,
        client_order_id=args.client_order_id
    )

    try:
        response = client.portfolios.list_portfolio_fills(request)
        print(response)
    except Exception as e:
        print(f"failed to list portfolio fills: {e}")


if __name__ == "__main__":
    main()

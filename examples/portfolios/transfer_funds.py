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
from intx_sdk.services.portfolios import TransferFundsRequest


def main():
    parser = argparse.ArgumentParser(description="Transfer funds between portfolios")
    parser.add_argument("--from-portfolio", required=True, help="Source portfolio ID")
    parser.add_argument("--to-portfolio", required=True, help="Destination portfolio ID")
    parser.add_argument("--asset", required=True, help="Asset symbol (e.g., USDC, BTC)")
    parser.add_argument("--amount", required=True, help="Amount to transfer")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = TransferFundsRequest(
        from_portfolio=args.from_portfolio,
        to_portfolio=args.to_portfolio,
        asset=args.asset,
        amount=args.amount
    )

    try:
        response = client.portfolios.transfer_funds(request)
        print(response)
    except Exception as e:
        print(f"failed to transfer funds: {e}")


if __name__ == "__main__":
    main()

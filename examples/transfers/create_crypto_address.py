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
from intx_sdk.services.transfers import CreateCryptoAddressRequest


def main():
    parser = argparse.ArgumentParser(
        description="Create crypto address",
        epilog="Example: --network-arn-id 'networks/ethereum-mainnet/assets/313ef8a9-ae5a-5f2f-8a56-572c0e2a4d5a'"
    )
    parser.add_argument("--portfolio", default=os.getenv('INTX_PORTFOLIO_ID'), help="Portfolio ID (defaults to INTX_PORTFOLIO_ID env var)")
    parser.add_argument("--asset", required=True, help="Asset symbol (e.g., ETH, USDC)")
    parser.add_argument("--network-arn-id", required=True, help="Network ARN ID (format: networks/{network}/assets/{asset-id})")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = CreateCryptoAddressRequest(
        portfolio=args.portfolio,
        asset=args.asset,
        network_arn_id=args.network_arn_id
    )

    try:
        response = client.transfers.create_crypto_address(request)
        print(response)
    except Exception as e:
        print(f"failed to create crypto address: {e}")


if __name__ == "__main__":
    main()

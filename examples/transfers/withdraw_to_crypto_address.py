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
from intx_sdk.services.transfers import WithdrawToCryptoAddressRequest


def main():
    parser = argparse.ArgumentParser(
        description="Withdraw to crypto address",
        epilog="""
Examples:
  # Withdraw USDC to Ethereum address
  python examples/transfers/withdraw_to_crypto_address.py --asset USDC --amount 1000 --address 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb --network-arn-id networks/ethereum-mainnet/assets/313ef8a9-ae5a-5f2f-8a56-572c0e2a4d5a --nonce 12345
"""
    )
    parser.add_argument("--asset", required=True, help="Asset symbol")
    parser.add_argument("--amount", required=True, help="Amount to withdraw")
    parser.add_argument("--address", required=True, help="Destination crypto address")
    parser.add_argument("--network-arn-id", required=True, help="Network ARN ID")
    parser.add_argument("--nonce", required=True, help="Nonce for idempotency")
    parser.add_argument("--add-network-fee-to-total", help="Add network fee to total (optional)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = WithdrawToCryptoAddressRequest(
        portfolio=os.getenv('INTX_PORTFOLIO_ID'),
        asset=args.asset,
        amount=args.amount,
        address=args.address,
        network_arn_id=args.network_arn_id,
        nonce=args.nonce,
        add_network_fee_to_total=args.add_network_fee_to_total
    )

    try:
        response = client.transfers.withdraw_to_crypto_address(request)
        print(response)
    except Exception as e:
        print(f"failed to withdraw to crypto address: {e}")


if __name__ == "__main__":
    main()

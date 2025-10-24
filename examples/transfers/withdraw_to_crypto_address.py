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
from intx_sdk.services.transfers import WithdrawToCryptoAddressRequest


def main():
    parser = argparse.ArgumentParser(description="Withdraw to crypto address")
    parser.add_argument("--portfolio", required=True, help="Portfolio ID")
    parser.add_argument("--asset", required=True, help="Asset symbol")
    parser.add_argument("--amount", required=True, help="Amount to withdraw")
    parser.add_argument("--address", required=True, help="Destination crypto address")
    parser.add_argument("--network-arn-id", required=True, help="Network ARN ID")
    parser.add_argument("--nonce", required=True, help="Nonce for idempotency")
    parser.add_argument("--add-network-fee-to-total", help="Add network fee to total (optional)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env("INTX_CREDENTIALS")

    request = WithdrawToCryptoAddressRequest(
        portfolio=args.portfolio,
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

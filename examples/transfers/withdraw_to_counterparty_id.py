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
from intx_sdk.services.transfers import WithdrawToCounterpartyIdRequest


def main():
    parser = argparse.ArgumentParser(description="Withdraw to counterparty ID")
    parser.add_argument("--portfolio", default=os.getenv('INTX_PORTFOLIO_ID'), help="Portfolio ID (defaults to INTX_PORTFOLIO_ID env var)")
    parser.add_argument("--counterparty-id", required=True, help="Counterparty ID")
    parser.add_argument("--asset", required=True, help="Asset symbol")
    parser.add_argument("--amount", required=True, help="Amount to withdraw")
    parser.add_argument("--nonce", required=True, help="Nonce for idempotency")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = WithdrawToCounterpartyIdRequest(
        portfolio=args.portfolio,
        counterparty_id=args.counterparty_id,
        asset=args.asset,
        amount=args.amount,
        nonce=args.nonce
    )

    try:
        response = client.transfers.withdraw_to_counterparty_id(request)
        print(response)
    except Exception as e:
        print(f"failed to withdraw to counterparty id: {e}")


if __name__ == "__main__":
    main()

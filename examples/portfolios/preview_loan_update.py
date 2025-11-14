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
from intx_sdk.services.portfolios import PreviewLoanUpdateRequest
from intx_sdk.enums import LoanAction


def main():
    parser = argparse.ArgumentParser(description="Preview loan update")
    parser.add_argument("--portfolio", required=True, help="Portfolio ID")
    parser.add_argument("--asset", required=True, help="Asset symbol")
    parser.add_argument("--action", required=True, help="Action: ACQUIRE or REPAY")
    parser.add_argument("--amount", required=True, help="Loan amount")
    args = parser.parse_args()

    client = IntxServicesClient.from_env("INTX_CREDENTIALS")

    request = PreviewLoanUpdateRequest(
        portfolio=args.portfolio,
        asset=args.asset,
        action=LoanAction[args.action],
        amount=args.amount
    )

    try:
        response = client.portfolios.preview_loan_update(request)
        print(response)
    except Exception as e:
        print(f"failed to preview loan update: {e}")


if __name__ == "__main__":
    main()

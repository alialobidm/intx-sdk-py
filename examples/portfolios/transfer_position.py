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
from intx_sdk.services.portfolios import TransferPositionRequest


def main():
    parser = argparse.ArgumentParser(description="Transfer position between portfolios")
    parser.add_argument("--from-portfolio", required=True, help="Source portfolio ID")
    parser.add_argument("--to-portfolio", required=True, help="Destination portfolio ID")
    parser.add_argument("--instrument", required=True, help="Instrument symbol")
    parser.add_argument("--quantity", required=True, help="Position quantity to transfer")
    parser.add_argument("--side", required=True, help="Position side: BUY or SELL")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = TransferPositionRequest(
        from_portfolio=args.from_portfolio,
        to_portfolio=args.to_portfolio,
        instrument=args.instrument,
        quantity=args.quantity,
        side=args.side
    )

    try:
        response = client.portfolios.transfer_position(request)
        print(response)
    except Exception as e:
        print(f"failed to transfer position: {e}")


if __name__ == "__main__":
    main()

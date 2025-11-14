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
from intx_sdk.services.orders import CancelOrdersRequest
from intx_sdk.enums import OrderSide, InstrumentType


def main():
    parser = argparse.ArgumentParser(description="Cancel multiple orders")
    parser.add_argument("--portfolio", required=True, help="Portfolio ID")
    parser.add_argument("--instrument", help="Instrument filter (optional)")
    parser.add_argument("--side", help="Side filter: BUY or SELL (optional)")
    parser.add_argument("--instrument-type", help="Instrument type filter: SPOT or PERP (optional)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = CancelOrdersRequest(
        portfolio=args.portfolio,
        instrument=args.instrument,
        side=OrderSide[args.side].value if args.side else None,
        instrument_type=InstrumentType[args.instrument_type].value if args.instrument_type else None
    )

    try:
        response = client.orders.cancel_orders(request)
        print(response)
    except Exception as e:
        print(f"failed to cancel orders: {e}")


if __name__ == "__main__":
    main()

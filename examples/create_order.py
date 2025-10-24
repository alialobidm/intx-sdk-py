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
from intx_sdk.services.orders import CreateOrderRequest


def main():
    parser = argparse.ArgumentParser(description="Create a new order")
    parser.add_argument("--portfolio", required=True, help="Portfolio ID")
    parser.add_argument("--instrument", required=True, help="Instrument symbol (e.g., BTC-PERP, ETH-PERP)")
    parser.add_argument("--side", required=True, help="Order side (BUY or SELL)")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", help="Limit price (optional)")
    parser.add_argument("--client-order-id", help="Client order ID (optional)")
    parser.add_argument("--time-in-force", help="Time in force (optional)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env("INTX_CREDENTIALS")

    request = CreateOrderRequest(
        portfolio=args.portfolio,
        instrument=args.instrument,
        side=args.side,
        quantity=args.quantity,
        price=args.price,
        client_order_id=args.client_order_id,
        time_in_force=args.time_in_force
    )

    try:
        response = client.orders.create_order(request)
        print(response)
    except Exception as e:
        print(f"failed to create order: {e}")


if __name__ == "__main__":
    main()

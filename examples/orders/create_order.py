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
from intx_sdk.enums import OrderSide, OrderType, TimeInForce


def main():
    parser = argparse.ArgumentParser(description="Create a new order")
    parser.add_argument("--client-order-id", required=True, help="Client order ID")
    parser.add_argument("--portfolio", required=True, help="Portfolio ID")
    parser.add_argument("--instrument", required=True, help="Instrument symbol (e.g., BTC-PERP, ETH-PERP)")
    parser.add_argument("--side", required=True, help="Order side (BUY or SELL)")
    parser.add_argument("--size", required=True, help="Order size")
    parser.add_argument("--type", required=True, help="Order type (LIMIT, MARKET, STOP_LIMIT, STOP, TAKE_PROFIT_STOP_LOSS)")
    parser.add_argument("--tif", required=True, help="Time in force (GTC, IOC, GTT, FOK)")
    parser.add_argument("--price", help="Limit price (optional)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env("INTX_CREDENTIALS")

    request = CreateOrderRequest(
        client_order_id=args.client_order_id,
        portfolio=args.portfolio,
        instrument=args.instrument,
        side=OrderSide[args.side],
        size=args.size,
        type=OrderType[args.type],
        tif=TimeInForce[args.tif],
        price=args.price
    )

    try:
        response = client.orders.create_order(request)
        print(response)
    except Exception as e:
        print(f"failed to create order: {e}")


if __name__ == "__main__":
    main()

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
import uuid
from intx_sdk import IntxServicesClient
from intx_sdk.services.orders import CreateOrderRequest
from intx_sdk.enums import OrderSide, OrderType, TimeInForce


def main():
    parser = argparse.ArgumentParser(description="Create a new order")
    parser.add_argument("--client-order-id", help="Client order ID (auto-generated if not provided)")
    parser.add_argument("--portfolio", default=os.getenv('INTX_PORTFOLIO_ID'), help="Portfolio ID (defaults to INTX_PORTFOLIO_ID env var)")
    parser.add_argument("--instrument", required=True, help="Instrument symbol (e.g., BTC-PERP, ETH-PERP)")
    parser.add_argument("--side", required=True, help="Order side (BUY or SELL)")
    parser.add_argument("--size", required=True, help="Order size")
    parser.add_argument("--type", default="LIMIT", help="Order type: LIMIT or MARKET (default: LIMIT)")
    parser.add_argument("--tif", default="GTC", help="Time in force: GTC, IOC, GTT, FOK (default: GTC)")
    parser.add_argument("--price", help="Limit price (required for LIMIT orders)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    # Generate client_order_id if not provided
    client_order_id = args.client_order_id or str(uuid.uuid4())

    # Validate: LIMIT orders require price
    order_type = args.type.upper()
    if order_type == "LIMIT" and not args.price:
        raise ValueError("--price is required for LIMIT orders")

    request = CreateOrderRequest(
        client_order_id=client_order_id,
        portfolio=args.portfolio,
        instrument=args.instrument,
        side=OrderSide[args.side.upper()].value,
        size=args.size,
        type=OrderType[order_type].value,
        tif=TimeInForce[args.tif.upper()].value,
        price=args.price
    )

    try:
        response = client.orders.create_order(request)
        print(response)
    except Exception as e:
        print(f"failed to create order: {e}")


if __name__ == "__main__":
    main()

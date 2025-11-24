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
from intx_sdk.services.orders import CancelOrderRequest


def main():
    parser = argparse.ArgumentParser(
        description="Cancel an order",
        epilog="""
Examples:
  # Cancel order
  python examples/orders/cancel_order.py --id 3jhx19me-1-0
"""
    )
    parser.add_argument("--id", required=True, help="Order ID to cancel")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = CancelOrderRequest(
        portfolio=os.getenv('INTX_PORTFOLIO_ID'),
        id=args.id
    )

    try:
        response = client.orders.cancel_order(request)
        print(response)
    except Exception as e:
        print(f"failed to cancel order: {e}")


if __name__ == "__main__":
    main()

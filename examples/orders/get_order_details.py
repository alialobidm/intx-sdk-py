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
from intx_sdk.services.orders import GetOrderDetailsRequest


def main():
    parser = argparse.ArgumentParser(description="Get order details")
    parser.add_argument("--portfolio", required=True, help="Portfolio ID")
    parser.add_argument("--order-id", required=True, help="Order ID")
    args = parser.parse_args()

    client = IntxServicesClient.from_env("INTX_CREDENTIALS")

    request = GetOrderDetailsRequest(
        portfolio=args.portfolio,
        order_id=args.order_id
    )

    try:
        response = client.orders.get_order_details(request)
        print(response)
    except Exception as e:
        print(f"failed to get order details: {e}")


if __name__ == "__main__":
    main()

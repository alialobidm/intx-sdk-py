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
from intx_sdk.services.orders import ListOpenOrdersRequest


def main():
    parser = argparse.ArgumentParser(description="List open orders")
    parser.add_argument("--portfolio", default=os.getenv('INTX_PORTFOLIO_ID'), help="Portfolio ID (defaults to INTX_PORTFOLIO_ID env var)")
    parser.add_argument("--instrument", help="Instrument filter (optional)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = ListOpenOrdersRequest(
        portfolio=args.portfolio,
        instrument=args.instrument
    )

    try:
        response = client.orders.list_open_orders(request)
        print(response)
    except Exception as e:
        print(f"failed to list open orders: {e}")


if __name__ == "__main__":
    main()

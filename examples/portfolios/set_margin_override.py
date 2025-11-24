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
from intx_sdk.services.portfolios import SetMarginOverrideRequest


def main():
    parser = argparse.ArgumentParser(
        description="Set margin override",
        epilog="""
Examples:
  # Set margin override
  python examples/portfolios/set_margin_override.py --margin-override 1.5
"""
    )
    parser.add_argument("--margin-override", required=True, help="Margin override value")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = SetMarginOverrideRequest(
        portfolio_id=os.getenv('INTX_PORTFOLIO_ID'),
        margin_override=args.margin_override
    )

    try:
        response = client.portfolios.set_margin_override(request)
        print(response)
    except Exception as e:
        print(f"failed to set margin override: {e}")


if __name__ == "__main__":
    main()

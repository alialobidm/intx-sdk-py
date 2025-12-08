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
from intx_sdk.services.portfolios import EnableDisableCrossCollateralRequest


def main():
    parser = argparse.ArgumentParser(
        description="Enable or disable cross collateral",
        epilog="""
Examples:
  # Enable cross collateral
  python examples/portfolios/enable_disable_cross_collateral.py --enabled true
"""
    )
    parser.add_argument("--enabled", required=True, help="Enable status: true or false")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = EnableDisableCrossCollateralRequest(
        portfolio=os.getenv('INTX_PORTFOLIO_ID'),
        enabled=args.enabled
    )

    try:
        response = client.portfolios.enable_disable_cross_collateral(request)
        print(response)
    except Exception as e:
        print(f"failed to enable/disable cross collateral: {e}")


if __name__ == "__main__":
    main()

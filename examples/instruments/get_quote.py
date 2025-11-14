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
from intx_sdk.services.instruments import GetQuotePerInstrumentRequest


def main():
    parser = argparse.ArgumentParser(description="Get quote for instrument")
    parser.add_argument("--instrument", required=True, help="Instrument symbol (e.g., BTC-PERP)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = GetQuotePerInstrumentRequest(instrument=args.instrument)

    try:
        response = client.instruments.get_quote_per_instrument(request)
        print(response)
    except Exception as e:
        print(f"failed to get quote: {e}")


if __name__ == "__main__":
    main()

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
from intx_sdk.services.instruments import GetAggregatedCandlesRequest
from intx_sdk.enums import Granularity


def main():
    parser = argparse.ArgumentParser(description="Get aggregated candles for instrument")
    parser.add_argument("--instrument", required=True, help="Instrument symbol (e.g., BTC-PERP)")
    parser.add_argument("--granularity", required=True, help="Candle granularity: ONE_MINUTE, FIVE_MINUTE, FIFTEEN_MINUTE, THIRTY_MINUTE, ONE_HOUR, TWO_HOUR, SIX_HOUR, ONE_DAY")
    parser.add_argument("--start", required=True, help="Start time")
    parser.add_argument("--end", help="End time (optional)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = GetAggregatedCandlesRequest(
        instrument=args.instrument,
        granularity=Granularity[args.granularity].value,
        start=args.start,
        end=args.end
    )

    try:
        response = client.instruments.get_aggregated_candles(request)
        print(response)
    except Exception as e:
        print(f"failed to get aggregated candles: {e}")


if __name__ == "__main__":
    main()

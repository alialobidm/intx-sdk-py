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
from intx_sdk.services.index import GetIndexCandlesRequest


def main():
    parser = argparse.ArgumentParser(description="Get index candles")
    parser.add_argument("--index", required=True, help="Index symbol")
    parser.add_argument("--granularity", required=True, help="Candle granularity (e.g., 1m, 5m, 1h)")
    parser.add_argument("--start", required=True, help="Start time")
    parser.add_argument("--end", help="End time (optional)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env("INTX_CREDENTIALS")

    request = GetIndexCandlesRequest(
        index=args.index,
        granularity=args.granularity,
        start=args.start,
        end=args.end
    )

    try:
        response = client.index.get_index_candles(request)
        print(response)
    except Exception as e:
        print(f"failed to get index candles: {e}")


if __name__ == "__main__":
    main()

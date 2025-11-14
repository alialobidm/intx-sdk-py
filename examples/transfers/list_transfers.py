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
from intx_sdk.services.transfers import ListTransfersRequest
from intx_sdk.enums import TransferType, TransferStatus


def main():
    parser = argparse.ArgumentParser(description="List transfers")
    parser.add_argument("--portfolios", help="Portfolio IDs filter (optional)")
    parser.add_argument("--status", help="Status filter: PROCESSED, NEW, FAILED, STARTED (optional)")
    parser.add_argument("--type", help="Type filter: DEPOSIT, WITHDRAW, INTERNAL, etc. (optional)")
    parser.add_argument("--time-from", help="Time from filter (optional)")
    parser.add_argument("--time-to", help="Time to filter (optional)")
    args = parser.parse_args()

    client = IntxServicesClient.from_env("INTX_CREDENTIALS")

    request = ListTransfersRequest(
        portfolios=args.portfolios,
        status=TransferStatus[args.status] if args.status else None,
        type=TransferType[args.type] if args.type else None,
        time_from=args.time_from,
        time_to=args.time_to
    )

    try:
        response = client.transfers.list_transfers(request)
        print(response)
    except Exception as e:
        print(f"failed to list transfers: {e}")


if __name__ == "__main__":
    main()

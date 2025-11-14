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
from intx_sdk.services.index import GetIndexCompositionRequest


def main():
    parser = argparse.ArgumentParser(description="Get index composition")
    parser.add_argument("--index", required=True, help="Index symbol")
    args = parser.parse_args()

    client = IntxServicesClient.from_env()

    request = GetIndexCompositionRequest(index=args.index)

    try:
        response = client.index.get_index_composition(request)
        print(response)
    except Exception as e:
        print(f"failed to get index composition: {e}")


if __name__ == "__main__":
    main()

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
from intx_sdk import IntxServicesClient
from intx_sdk.services.positionoffsets import ListPositionOffsetsRequest


def main():
    client = IntxServicesClient.from_env()

    request = ListPositionOffsetsRequest()

    try:
        response = client.positionoffsets.list_position_offsets(request)
        print(response)
    except Exception as e:
        print(f"failed to list position offsets: {e}")


if __name__ == "__main__":
    main()

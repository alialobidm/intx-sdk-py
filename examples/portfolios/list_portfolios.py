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

import json
from intx_sdk import IntxServicesClient
from intx_sdk.services.portfolios import ListPortfoliosRequest


def main():
    client = IntxServicesClient.from_env("INTX_CREDENTIALS")
    request = ListPortfoliosRequest()
    response = client.portfolios.list_portfolios(request)
    portfolios = [vars(portfolio) for portfolio in response.portfolios]
    print(json.dumps(portfolios, indent=2))


if __name__ == "__main__":
    main()

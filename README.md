# Coinbase International Exchange (INTX) Python SDK

## Overview

The *INTX Python SDK* is a sample library that demonstrates the usage of the [Coinbase International Exchange (INTX)](https://international.coinbase.com/) API via its [REST APIs](https://docs.cdp.coinbase.com/intx/reference). This SDK provides a structured way to integrate Coinbase INTX functionalities into your Python applications.
## License

The *INTX Python SDK* sample library is free and open source and released under the [Apache License, Version 2.0](LICENSE).

The application and code are only available for demonstration purposes.

## Installation

```bash
pip install intx-sdk-py
```

Or install from source:

```bash
git clone https://github.com/coinbase-samples/intx-sdk-py.git
cd intx-sdk-py
pip install -e .
```

## Authentication

To use the INTX Python SDK, you will need to create API credentials in the [INTX web console](https://international.coinbase.com/) under Settings -> API.

Credentials can be stored as environment variables or passed directly. The SDK supports two initialization patterns:

### Using Environment Variables (Recommended)

Set the following environment variable with your API credentials in JSON format:

```bash
export INTX_CREDENTIALS='{
  "accessKey": "your-access-key",
  "passphrase": "your-passphrase",
  "signingKey": "your-signing-key"
}'
```

Then initialize the client:

```python
from intx_sdk import IntxServicesClient

client = IntxServicesClient.from_env("INTX_CREDENTIALS")
```

### Using Credentials Object

```python
from intx_sdk import IntxServicesClient
from intx_sdk.credentials import Credentials

credentials = Credentials(
    access_key="your-access-key",
    passphrase="your-passphrase",
    signing_key="your-signing-key"
)

client = IntxServicesClient(credentials)
```

## Environment Configuration

By default, the SDK uses the production environment. To use the sandbox environment, set the `INTX_ENVIRONMENT` environment variable:

```bash
export INTX_ENVIRONMENT=sandbox
```

## Usage

```python
from intx_sdk import IntxServicesClient
from intx_sdk.services.portfolios import ListPortfoliosRequest

client = IntxServicesClient.from_env("INTX_CREDENTIALS")

# List portfolios
request = ListPortfoliosRequest()
response = client.portfolios.list_portfolios(request)
print(response)
```

For more examples, see the [examples](examples/) directory.
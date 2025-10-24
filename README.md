# Coinbase International Exchange (INTX) Python SDK

## Overview

The *INTX Python SDK* is a sample library that demonstrates the usage of the [Coinbase International Exchange (INTX) API](https://docs.cdp.coinbase.com/intx/reference) for trading perpetual futures and managing portfolios. This SDK provides a structured way to integrate Coinbase INTX functionalities into your Python applications.

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

## Specifying the Environment

INTX supports both production and sandbox environments. You can specify the desired environment by setting the base URL when initializing the client:

```python
from intx_sdk import IntxServicesClient

# Production (default)
client = IntxServicesClient.from_env("INTX_CREDENTIALS")

# Sandbox
client = IntxServicesClient.from_env(
    "INTX_CREDENTIALS",
    base_url="https://api-n5e1.coinbase.com/api/v1"
)
```

## Usage

The SDK provides a unified client interface for all INTX services. Each service is accessible as a property on the client:

### Services Client (Recommended)

```python
from intx_sdk import IntxServicesClient
from intx_sdk.services.portfolios import ListPortfoliosRequest

client = IntxServicesClient.from_env("INTX_CREDENTIALS")

# List portfolios
request = ListPortfoliosRequest()
try:
    response = client.portfolios.list_portfolios(request)
    print(response)
except Exception as e:
    print(f"failed to list portfolios: {e}")
```

### Available Services

The SDK provides access to the following services:

- **Portfolios** - Manage portfolios, balances, positions, and portfolio settings
- **Orders** - Create, modify, cancel, and query orders
- **Assets** - Query supported assets and their properties
- **Instruments** - Query available trading instruments
- **Transfers** - Manage deposits, withdrawals, and transfers
- **Fee Rates** - Query fee rate information
- **Position Offsets** - Manage position offsets
- **Rankings** - Query leaderboard and rankings data

## Examples

The [examples](examples/) directory contains sample code demonstrating various SDK capabilities:

### Portfolio Management
- [list_portfolios.py](examples/list_portfolios.py) - List all portfolios
- [create_portfolio.py](examples/create_portfolio.py) - Create a new portfolio
- [get_portfolio_details.py](examples/get_portfolio_details.py) - Get detailed portfolio information
- [get_portfolio_summary.py](examples/get_portfolio_summary.py) - Get portfolio summary
- [list_portfolio_balances.py](examples/list_portfolio_balances.py) - List portfolio balances
- [list_portfolio_fills.py](examples/list_portfolio_fills.py) - List portfolio fill history
- [transfer_funds.py](examples/transfer_funds.py) - Transfer funds between portfolios

### Order Management
- [create_order.py](examples/create_order.py) - Create a new order
- [list_open_orders.py](examples/list_open_orders.py) - List open orders
- [get_order_details.py](examples/get_order_details.py) - Get order details
- [modify_order.py](examples/modify_order.py) - Modify an open order
- [cancel_order.py](examples/cancel_order.py) - Cancel an order

### Market Data
- [list_assets.py](examples/list_assets.py) - List supported assets
- [list_instruments.py](examples/list_instruments.py) - List trading instruments

### Transfers
- [list_transfers.py](examples/list_transfers.py) - List transfers
- [withdraw_to_crypto_address.py](examples/withdraw_to_crypto_address.py) - Withdraw to a crypto address

### Running Examples

Each example uses argparse for command-line arguments:

```bash
# List portfolios
python examples/list_portfolios.py

# Create an order
python examples/create_order.py \
  --portfolio your-portfolio-id \
  --instrument BTC-PERP \
  --side BUY \
  --quantity 0.01 \
  --price 50000

# List open orders for a portfolio
python examples/list_open_orders.py \
  --portfolio your-portfolio-id \
  --instrument BTC-PERP

# Get portfolio details
python examples/get_portfolio_details.py \
  --portfolio your-portfolio-id
```

## Supported Python Versions

The SDK is tested and confirmed to work with Python 3.8 and newer.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Resources

- [INTX API Documentation](https://docs.cdp.coinbase.com/intx/reference)
- [INTX Website](https://international.coinbase.com/)

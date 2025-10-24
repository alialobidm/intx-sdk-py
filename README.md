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

The [examples](examples/) directory contains **58 comprehensive examples** organized by service, covering all SDK endpoints:

### [Portfolios](examples/portfolios/) (28 examples)
- [list_portfolios.py](examples/portfolios/list_portfolios.py) - List all portfolios
- [create_portfolio.py](examples/portfolios/create_portfolio.py) - Create a new portfolio
- [get_portfolio.py](examples/portfolios/get_portfolio.py) - Get portfolio information
- [get_portfolio_details.py](examples/portfolios/get_portfolio_details.py) - Get detailed portfolio information
- [get_portfolio_summary.py](examples/portfolios/get_portfolio_summary.py) - Get portfolio summary
- [update_portfolio.py](examples/portfolios/update_portfolio.py) - Update portfolio name
- [patch_portfolio.py](examples/portfolios/patch_portfolio.py) - Patch portfolio settings
- [list_portfolio_balances.py](examples/portfolios/list_portfolio_balances.py) - List portfolio balances
- [get_balance_for_portfolio_asset.py](examples/portfolios/get_balance_for_portfolio_asset.py) - Get balance for specific asset
- [list_portfolio_positions.py](examples/portfolios/list_portfolio_positions.py) - List all positions in a portfolio
- [get_position_for_instrument.py](examples/portfolios/get_position_for_instrument.py) - Get position for specific instrument
- [list_portfolio_fills.py](examples/portfolios/list_portfolio_fills.py) - List portfolio fill history
- [list_fills_by_portfolios.py](examples/portfolios/list_fills_by_portfolios.py) - List fills across multiple portfolios
- [list_portfolio_fee_rates.py](examples/portfolios/list_portfolio_fee_rates.py) - List fee rates for portfolios
- [transfer_funds.py](examples/portfolios/transfer_funds.py) - Transfer funds between portfolios
- [transfer_position.py](examples/portfolios/transfer_position.py) - Transfer position between portfolios
- [get_fund_transfer_limit.py](examples/portfolios/get_fund_transfer_limit.py) - Get fund transfer limits
- [enable_disable_auto_margin.py](examples/portfolios/enable_disable_auto_margin.py) - Enable/disable auto margin
- [enable_disable_cross_collateral.py](examples/portfolios/enable_disable_cross_collateral.py) - Enable/disable cross collateral
- [set_margin_override.py](examples/portfolios/set_margin_override.py) - Set margin override
- [list_active_loans.py](examples/portfolios/list_active_loans.py) - List active loans for a portfolio
- [get_loan_info_for_portfolio_asset.py](examples/portfolios/get_loan_info_for_portfolio_asset.py) - Get loan info for asset
- [get_asset_loan_availability.py](examples/portfolios/get_asset_loan_availability.py) - Get asset loan availability
- [acquire_or_repay_loan.py](examples/portfolios/acquire_or_repay_loan.py) - Acquire or repay a loan
- [preview_loan_update.py](examples/portfolios/preview_loan_update.py) - Preview loan update
- [get_open_position_limits_for_portfolio_instrument.py](examples/portfolios/get_open_position_limits_for_portfolio_instrument.py) - Get position limits for instrument
- [list_open_position_limits_for_all_instruments.py](examples/portfolios/list_open_position_limits_for_all_instruments.py) - List position limits for all instruments
- [get_total_open_position_limit.py](examples/portfolios/get_total_open_position_limit.py) - Get total position limit

### [Orders](examples/orders/) (6 examples)
- [create_order.py](examples/orders/create_order.py) - Create a new order
- [list_open_orders.py](examples/orders/list_open_orders.py) - List open orders
- [get_order_details.py](examples/orders/get_order_details.py) - Get order details
- [modify_order.py](examples/orders/modify_order.py) - Modify an open order
- [cancel_order.py](examples/orders/cancel_order.py) - Cancel an order
- [cancel_orders.py](examples/orders/cancel_orders.py) - Cancel multiple orders with filters

### [Instruments](examples/instruments/) (6 examples)
- [list_instruments.py](examples/instruments/list_instruments.py) - List trading instruments
- [get_instrument_details.py](examples/instruments/get_instrument_details.py) - Get details for a specific instrument
- [get_quote.py](examples/instruments/get_quote.py) - Get current quote for an instrument
- [get_historical_funding_rates.py](examples/instruments/get_historical_funding_rates.py) - Get historical funding rates
- [get_daily_trading_volumes.py](examples/instruments/get_daily_trading_volumes.py) - Get daily trading volumes
- [get_aggregated_candles.py](examples/instruments/get_aggregated_candles.py) - Get aggregated price candles

### [Transfers](examples/transfers/) (7 examples)
- [list_transfers.py](examples/transfers/list_transfers.py) - List transfers
- [get_transfer.py](examples/transfers/get_transfer.py) - Get details for a specific transfer
- [create_crypto_address.py](examples/transfers/create_crypto_address.py) - Create a crypto deposit address
- [withdraw_to_crypto_address.py](examples/transfers/withdraw_to_crypto_address.py) - Withdraw to a crypto address
- [create_counterparty_id.py](examples/transfers/create_counterparty_id.py) - Create a counterparty ID
- [validate_counterparty_id.py](examples/transfers/validate_counterparty_id.py) - Validate a counterparty ID
- [withdraw_to_counterparty_id.py](examples/transfers/withdraw_to_counterparty_id.py) - Withdraw to a counterparty ID

### [Assets](examples/assets/) (3 examples)
- [list_assets.py](examples/assets/list_assets.py) - List supported assets
- [get_asset_details.py](examples/assets/get_asset_details.py) - Get details for a specific asset
- [get_supported_networks.py](examples/assets/get_supported_networks.py) - Get supported networks for an asset

### [Index](examples/index/) (4 examples)
- [get_index_price.py](examples/index/get_index_price.py) - Get index price
- [get_index_composition.py](examples/index/get_index_composition.py) - Get index composition
- [get_index_composition_history.py](examples/index/get_index_composition_history.py) - Get index composition history
- [get_index_candles.py](examples/index/get_index_candles.py) - Get index candles

### [Fee Rates](examples/feerates/) (1 example)
- [list_fee_rate_tiers.py](examples/feerates/list_fee_rate_tiers.py) - List fee rate tiers

### [Address Book](examples/addressbook/) (1 example)
- [get_address_book.py](examples/addressbook/get_address_book.py) - Get address book

### [Position Offsets](examples/positionoffsets/) (1 example)
- [list_position_offsets.py](examples/positionoffsets/list_position_offsets.py) - List position offsets

### [Rankings](examples/rankings/) (1 example)
- [get_rankings.py](examples/rankings/get_rankings.py) - Get leaderboard rankings

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

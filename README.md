# Algorithmic Backtest: Golden Cross Strategy

A simple Python backtesting project that evaluates a classic moving-average crossover strategy against a buy-and-hold benchmark using historical market data.

## Overview

This project tests whether a Golden Cross strategy (50-day moving average crossing above a 200-day moving average) would have outperformed simply buying and holding Apple (AAPL) stock over the past five years.

The script downloads historical price data, generates trading signals, simulates portfolio performance, and plots the strategy against a benchmark.

## Strategy

The Golden Cross strategy is a trend-following system:

- Buy when the 50-day moving average rises above the 200-day moving average
- Sell when the 50-day moving average falls below the 200-day moving average

This project compares the strategy to a benchmark of holding the asset without rebalancing.

## What the script does

- Downloads 5 years of historical OHLCV data from Yahoo Finance
- Computes 50-day and 200-day moving averages
- Generates bullish/bearish signal states
- Simulates portfolio value using daily returns
- Compares strategy returns to buy-and-hold returns
- Saves a chart to `backtest_results.png`

## Example output

A typical run produces results like this:

```text
--- Backtest Results: AAPL ---
Initial Capital: $10,000
Buy & Hold Final Value: $15,795.00
Strategy Final Value: $8,299.00
Strategy vs Buy & Hold: -47.46%
```

These results show that the strategy underperformed buy-and-hold in this case, which is a useful reminder that a strategy can look logical but still fail in practice.

## Installation

```bash
pip install -r requirements.txt
```

## Run the backtest

```bash
python backtest.py
```

## Project structure

```text
algorithmic-backtest/
├── backtest.py
├── requirements.txt
├── README.md
└── backtest_results.png   # generated when the script runs
```

## Dependencies

- pandas
- numpy
- matplotlib
- yfinance

## Notes

- The backtest uses a delayed signal (`Signal.shift(1)`) to reduce lookahead bias.
- It does not include transaction costs, taxes, or slippage.
- This is a learning-focused example rather than a production trading system.

## License

This project is provided for educational and research purposes only.

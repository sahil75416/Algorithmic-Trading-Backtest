import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta


def get_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end, progress=False)
    if data.empty:
        print(f"No data found for {ticker}")
        return None
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()
    data.dropna(inplace=True)
    print(f"Fetched {len(data)} rows for {ticker}")
    return data


def generate_signals(data):
    data['Signal'] = np.where(data['MA50'] > data['MA200'], 1, 0)
    data['Position'] = data['Signal'].diff()
    return data


def backtest(data, initial_capital=10000):
    data['Daily_Return'] = data['Close'].pct_change()
    data['Strategy_Return'] = data['Daily_Return'] * data['Signal'].shift(1)
    data['Buy_Hold_Value'] = initial_capital * (1 + data['Daily_Return']).cumprod()
    data['Strategy_Value'] = initial_capital * (1 + data['Strategy_Return']).cumprod()
    return data


def plot_results(data, ticker):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data.index, data['Buy_Hold_Value'], color="blue", label="Buy & Hold")
    ax.plot(data.index, data['Strategy_Value'], color="red", label="Golden Cross Strategy")
    ax.set_xlabel("Date")
    ax.set_ylabel("Portfolio Value ($)")
    ax.set_title(f"Golden Cross Strategy vs Buy & Hold — {ticker}")
    ax.legend()
    plt.tight_layout()
    plt.savefig("backtest_results.png")
    plt.show()


if __name__ == "__main__":
    ticker = "AAPL"
    start = datetime.now() - timedelta(days=365*5)
    end = datetime.now()

    data = get_data(ticker, start, end)
    if data is None:
        print("Exiting — no data available.")
        exit()

    data = generate_signals(data)
    data = backtest(data)

    final_strategy = data['Strategy_Value'].iloc[-1]
    final_buyhold = data['Buy_Hold_Value'].iloc[-1]

    print(f"\n--- Backtest Results: {ticker} ---")
    print(f"Initial Capital: $10,000")
    print(f"Buy & Hold Final Value: ${final_buyhold:,.2f}")
    print(f"Strategy Final Value: ${final_strategy:,.2f}")
    print(f"Strategy vs Buy & Hold: {((final_strategy/final_buyhold)-1)*100:.2f}%")

    plot_results(data, ticker)
from __future__ import annotations

import argparse

from bot.backtest import SimpleBacktester
from bot.config import BotConfig
from bot.strategy import MovingAverageCrossStrategy


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bot de trading - backtest local")
    parser.add_argument(
        "--prices",
        required=True,
        help="Série de prix séparés par des virgules, ex: 100,101,102",
    )
    parser.add_argument("--initial-cash", type=float, default=10_000.0)
    parser.add_argument("--short-window", type=int, default=3)
    parser.add_argument("--long-window", type=int, default=5)
    parser.add_argument("--trade-size", type=float, default=1.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prices = [float(p.strip()) for p in args.prices.split(",") if p.strip()]

    if not prices:
        raise ValueError("Aucun prix fourni")

    config = BotConfig(
        initial_cash=args.initial_cash,
        short_window=args.short_window,
        long_window=args.long_window,
        trade_size=args.trade_size,
    )
    config.validate()

    strategy = MovingAverageCrossStrategy(
        short_window=config.short_window,
        long_window=config.long_window,
    )
    backtester = SimpleBacktester(
        initial_cash=config.initial_cash,
        trade_size=config.trade_size,
    )

    for price in prices:
        signal = strategy.on_price(price)
        backtester.step(price, signal)
        print(f"price={price:.2f} signal={signal}")

    result = backtester.result(prices[-1])
    print("\n=== Résultat ===")
    print(f"Cash final: {result.final_cash}")
    print(f"Position finale: {result.final_position}")
    print(f"Valeur finale: {result.final_value}")
    print(f"Nombre de trades: {result.trades}")


if __name__ == "__main__":
    main()

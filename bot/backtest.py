from __future__ import annotations

from dataclasses import dataclass

from bot.strategy import Signal


@dataclass
class BacktestResult:
    final_cash: float
    final_position: float
    final_value: float
    trades: int


class SimpleBacktester:
    def __init__(self, initial_cash: float, trade_size: float) -> None:
        if initial_cash <= 0:
            raise ValueError("initial_cash doit être > 0")
        if trade_size <= 0:
            raise ValueError("trade_size doit être > 0")

        self.cash = initial_cash
        self.position = 0.0
        self.trade_size = trade_size
        self.trades = 0

    def step(self, price: float, signal: Signal) -> None:
        if price <= 0:
            raise ValueError("price doit être > 0")

        if signal == Signal.BUY:
            cost = price * self.trade_size
            if self.cash >= cost:
                self.cash -= cost
                self.position += self.trade_size
                self.trades += 1

        elif signal == Signal.SELL:
            if self.position >= self.trade_size:
                self.cash += price * self.trade_size
                self.position -= self.trade_size
                self.trades += 1

    def result(self, last_price: float) -> BacktestResult:
        if last_price <= 0:
            raise ValueError("last_price doit être > 0")

        final_value = self.cash + self.position * last_price
        return BacktestResult(
            final_cash=round(self.cash, 2),
            final_position=round(self.position, 8),
            final_value=round(final_value, 2),
            trades=self.trades,
        )

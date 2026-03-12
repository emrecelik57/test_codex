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
        self.cash = initial_cash
        self.position = 0.0
        self.trade_size = trade_size
        self.trades = 0

    def step(self, price: float, signal: Signal) -> None:
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
        final_value = self.cash + self.position * last_price
        return BacktestResult(
            final_cash=round(self.cash, 2),
            final_position=round(self.position, 8),
            final_value=round(final_value, 2),
            trades=self.trades,
        )

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from enum import Enum


class Signal(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


@dataclass
class MovingAverageCrossStrategy:
    short_window: int
    long_window: int

    def __post_init__(self) -> None:
        if self.short_window <= 0 or self.long_window <= 0:
            raise ValueError("Les fenêtres doivent être positives")
        if self.short_window >= self.long_window:
            raise ValueError("short_window doit être < long_window")

        self._short_prices = deque(maxlen=self.short_window)
        self._long_prices = deque(maxlen=self.long_window)
        self._previous_state: int | None = None

    def _avg(self, values: deque[float]) -> float:
        return sum(values) / len(values)

    def on_price(self, price: float) -> Signal:
        self._short_prices.append(price)
        self._long_prices.append(price)

        if len(self._long_prices) < self.long_window:
            return Signal.HOLD

        short_ma = self._avg(self._short_prices)
        long_ma = self._avg(self._long_prices)
        state = 1 if short_ma > long_ma else -1 if short_ma < long_ma else 0

        if self._previous_state is None:
            self._previous_state = state
            return Signal.HOLD

        if self._previous_state <= 0 and state > 0:
            self._previous_state = state
            return Signal.BUY

        if self._previous_state >= 0 and state < 0:
            self._previous_state = state
            return Signal.SELL

        self._previous_state = state
        return Signal.HOLD

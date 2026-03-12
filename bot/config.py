from dataclasses import dataclass


@dataclass
class BotConfig:
    initial_cash: float = 10_000.0
    short_window: int = 3
    long_window: int = 5
    trade_size: float = 1.0

    def validate(self) -> None:
        if self.initial_cash <= 0:
            raise ValueError("initial_cash doit être > 0")
        if self.trade_size <= 0:
            raise ValueError("trade_size doit être > 0")
        if self.short_window < 1:
            raise ValueError("short_window doit être >= 1")
        if self.long_window < 2:
            raise ValueError("long_window doit être >= 2")
        if self.short_window >= self.long_window:
            raise ValueError("short_window doit être strictement inférieur à long_window")

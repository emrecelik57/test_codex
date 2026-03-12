import pytest

from bot.backtest import SimpleBacktester
from bot.strategy import Signal


def test_backtester_updates_cash_position() -> None:
    bt = SimpleBacktester(initial_cash=1000, trade_size=1)

    bt.step(100, Signal.BUY)
    bt.step(120, Signal.SELL)

    result = bt.result(120)
    assert result.final_cash == 1020
    assert result.final_position == 0
    assert result.trades == 2


def test_backtester_validates_initial_values() -> None:
    with pytest.raises(ValueError, match="initial_cash"):
        SimpleBacktester(initial_cash=0, trade_size=1)

    with pytest.raises(ValueError, match="trade_size"):
        SimpleBacktester(initial_cash=1000, trade_size=0)


def test_backtester_validates_price_values() -> None:
    bt = SimpleBacktester(initial_cash=1000, trade_size=1)

    with pytest.raises(ValueError, match="price"):
        bt.step(0, Signal.HOLD)

    with pytest.raises(ValueError, match="last_price"):
        bt.result(0)

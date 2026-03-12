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

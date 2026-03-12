from bot.strategy import MovingAverageCrossStrategy, Signal


def test_strategy_generates_buy_and_sell() -> None:
    strategy = MovingAverageCrossStrategy(short_window=2, long_window=3)
    prices = [10, 10, 10, 11, 12, 11, 10, 9]

    signals = [strategy.on_price(p) for p in prices]

    assert Signal.BUY in signals
    assert Signal.SELL in signals

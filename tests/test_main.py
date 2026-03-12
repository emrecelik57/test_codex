import pytest

from bot.main import parse_prices


def test_parse_prices_happy_path() -> None:
    assert parse_prices("100, 101.5,102") == [100.0, 101.5, 102.0]


def test_parse_prices_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="Aucun prix"):
        parse_prices(" , , ")


def test_parse_prices_rejects_non_numeric() -> None:
    with pytest.raises(ValueError, match="valeur invalide"):
        parse_prices("100,abc,101")


def test_parse_prices_rejects_non_positive_values() -> None:
    with pytest.raises(ValueError, match="doivent être > 0"):
        parse_prices("100,0,101")

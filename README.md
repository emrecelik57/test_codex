# Bot de Trading (Python)

Ce projet fournit une base propre pour créer un **bot de trading** avec :

- une stratégie simple (croisement de moyennes mobiles) ;
- un mode **paper trading/backtest** sans risque réel ;
- une architecture extensible pour brancher une API d'exchange plus tard.

## Structure

- `bot/config.py` : paramètres du bot.
- `bot/strategy.py` : logique de stratégie.
- `bot/backtest.py` : moteur de simulation.
- `bot/main.py` : point d'entrée CLI.
- `tests/` : tests unitaires.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Lancer un backtest rapide

```bash
python -m bot.main --prices "100,101,102,103,102,101,100,99,100,101,102"
```

## Exemple sortie attendue

- Signaux BUY / SELL selon le croisement MA courte / MA longue
- Résumé final : cash, position, valeur totale, nombre de trades

## Avertissement

Ce code est pédagogique. N'utilisez pas ce bot en réel sans gestion du risque avancée,
monitoring, limites d'exposition et revue de sécurité.

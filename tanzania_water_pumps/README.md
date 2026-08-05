# Tanzanian Water Pumps — analyse et stratégie de réparation

Réponse au cas « Tanzanian Water Pumps » : à partir du recensement de 59 400 points d'eau du
Ministère de l'Eau de Tanzanie, identifier les pompes hors service et construire une stratégie
d'intervention qui maximise l'accès à l'eau à budget donné.

L'énoncé du cas est repris dans [`Case_description.pdf`](Case_description.pdf).

## Contenu

```
tanzania_water_pumps/
├── water_pumps_analysis.ipynb   ← l'analyse complète (exécutée, sorties incluses)
├── data/raw/                    ← données fournies, compressées en .csv.gz
│   ├── training_set_values.csv.gz
│   ├── training_set_labels.csv.gz
│   └── test_set_values.csv.gz
└── outputs/                     ← produits par le notebook
    ├── test_set_predictions.csv ← état prédit des 14 850 pompes du jeu de test
    └── intervention_plan.csv    ← plan d'intervention priorisé (score, action, tranche P1-P4)
```

## Déroulé du notebook

| Section | Contenu |
|---|---|
| 1 | Cadrage, chargement, audit de qualité (sentinelles, redondances, valeurs manquantes) |
| 2 | Nettoyage et variables dérivées, appliqués identiquement au train et au test |
| 3 | Diagnostic : disponibilité de l'eau, âge, technologie, gouvernance, géographie |
| 4 | Modélisation : références, gradient boosting « terrain » vs « à distance », validation croisée |
| 5 | Décision : score de priorité, courbe de couverture, arbre réparer/remplacer, chiffrage |
| 6 | Livrables : prédictions et plan d'intervention sur le jeu de test |
| 7 | Synthèse, recommandations et limites |

## Résultats principaux

- **38 % du parc est hors service**, soit environ 3,9 M de personnes concernées.
- Le modèle « à distance » (sans aucune information relevée sur place) atteint **0,78 d'exactitude**
  et **0,90 d'AUC** sur la détection des pompes hors service — validé sur 5 découpages.
- En inspectant **20 % du parc** guidé par le modèle, on retrouve **49 % des pompes en panne**
  (contre 20 % au hasard) : la même détection pour 60 % de déplacements en moins.
- Prioriser sur le **risque seul est moins efficace qu'une tournée au hasard** en personnes
  reconnectées par euro. C'est la pondération **risque × population desservie** qui crée la valeur.

## Reproduire

```bash
pip install -r requirements.txt
jupyter lab water_pumps_analysis.ipynb      # ou :
jupyter nbconvert --to notebook --execute --inplace water_pumps_analysis.ipynb
```

Le notebook s'exécute de bout en bout en ~2 minutes et doit être lancé depuis ce répertoire
(les chemins `data/raw` et `outputs` sont relatifs).

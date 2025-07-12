# Projet de Surveillance Intelligente en Python

## Contexte

Ce projet est réalisé dans le cadre du module **Programmation Avancée en Python**.  
Il consiste à développer un système de **surveillance intelligent** qui :

- lit un fichier de logs JSON de manière asynchrone,
- détecte des anomalies (3 événements critiques en moins de 30 secondes),
- enregistre les alertes dans un fichier JSON,
- génère un **rapport PDF** des événements et alertes,
- affiche des visualisations statistiques,
- et fournit une interface CLI (menu interactif).

---

## Structure du projet

``` bash
Projet_Surveillance/
│
├── main.py # Point d'entrée CLI (menu)
├── event.py # Classes Event, EventAnalyzer, EventLogger
├── reader.py # Lecture asynchrone des logs
├── reporter.py # Génération du rapport PDF
├── visualizer.py # Histogrammes matplotlib
├── events.log # Fichier log JSON simulé
├── alerts.json # Alertes détectées
├── traceback.log # Journalisation des traitements
├── requirements.txt # Dépendances Python
└── README.md # Ce fichier

```

## Créer un environnement virtuel

``` bash
python -m venv venv
# Sous Windows
venv\Scripts\activate
# Sous Linux / Mac
source venv/bin/activate
```

## Installer les dépendances

``` bash
pip install -r requirements.txt

```

## Lancer la CLI

``` bash

python main.py

```

## Lien de mon repository GitHub

[https://github.com/Al4567/PROJET-PYTHON-AVANCE-MASTER-PREMIERE-ANNEE](https://github.com/Al4567/PROJET-PYTHON-AVANCE-MASTER-PREMIERE-ANNEE)

## Lien de la video pour la démonstration

[lien de la vidéo pour la démo](https://www.loom.com/share/e9c6b536aec742b383710e0b58702c4c?sid=efd714ad-c8a5-4cc1-aade-87dc64be499f)

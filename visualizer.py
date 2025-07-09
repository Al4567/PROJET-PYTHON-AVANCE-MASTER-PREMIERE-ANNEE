# histogramme matplotlib

"""
Module pour la visualisation statistique des événements traités.

Génère un histogramme du nombre d'événements par niveau (INFO, WARN, ERROR, CRITICAL)
en utilisant matplotlib.
"""

import matplotlib.pyplot as plt
from collections import Counter

def plot_events(analyzer):
    """
    Crée et affiche un histogramme montrant le nombre d'événements
    par niveau de log.

    Parameters
    ----------
    analyzer : EventAnalyzer
        Instance contenant les événements analysés.
    """

    levels = [e.level for e in analyzer.events]
    counts = Counter(levels)
    plt.bar(counts.keys(), counts.values(), color="skyblue")
    plt.title("Nombre d'événements par niveau")
    plt.xlabel("Niveau")
    plt.ylabel("Fréquence")
    plt.show()
# Lecture asynchrone des logs
"""
Module pour la lecture asynchrone du fichier events.log.

Lit chaque ligne (événement JSON) toutes les 2 secondes,
puis crée un objet Event et le traite via EventAnalyzer et EventLogger.
"""

import asyncio
import json
from event import Event


async def read_log_file(filepath, analyzer, logger):
    
    """
    Lecture asynchrone du fichier log ligne par ligne avec pause de 2 secondes.

    Parameters
    ----------
    filepath : str
        Chemin vers le fichier log (ex: 'events.log').
    analyzer : EventAnalyzer
        Instance qui gère l'ajout d'événements et la détection d'anomalies.
    logger : EventLogger
        Logger pour enregistrer les traitements dans un fichier système.
    """
    with open(filepath, "r") as f:
        for line in f:
            await asyncio.sleep(2)
            data = json.loads(line.strip())
            event = Event(
                timestamp=data["timestamp"],
                level=data["level"],
                message=data["message"]
            )
            analyzer.add_event(event)
            logger.log(f"Event traité: {event.level} - {event.message}")

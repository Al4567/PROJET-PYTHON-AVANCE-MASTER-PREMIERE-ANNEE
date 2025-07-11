# class Event , EventAnalyser,Eventlogger

# event.py

"""
event.py
---------
Contient les classes :
- Event : représente un événement individuel.
- EventAnalyzer : analyse les événements pour détecter des anomalies et produire des alertes.
- EventLogger : enregistre les événements traités dans un fichier log.
"""
import datetime
import logging
import json

class Event:
    """
    Représente un événement lu depuis le fichier log.
    
    Attributs :
    ----------
    timestamp : datetime
        Date et heure de l'événement.
    level : str
        Niveau de gravité (INFO, WARN, ERROR, CRITICAL).
    message : str
        Message associé à l'événement.
    """
    
    def __init__(self, timestamp, level, message):
        """
        Initialise un nouvel objet Event.
        
        Parameters
        ----------
        timestamp : str
            Horodatage au format ISO (ex: "2025-06-30T12:00:00Z").
        level : str
            Niveau de log (INFO, WARN, ERROR, CRITICAL).
        message : str
            Description du message.
        """
        self.timestamp = datetime.datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        self.level = level
        self.message = message

class EventAnalyzer:
    
    """
    Analyseur des événements pour détecter les anomalies et stocker les alertes.
    
    Attributs :
    ----------
    events : list
        Liste de tous les événements traités.
    alerts : list
        Liste des alertes détectées (3 événements critiques en moins de 30s).
    """
    def __init__(self):
        self.events = []
        self.alerts = []

    def add_event(self, event):
        """
        Ajoute un événement à la liste et vérifie s'il déclenche une alerte.
        
        Parameters
        ----------
        event : Event
            L'événement à ajouter.
        """
        self.events.append(event)
        self.detect_anomaly()

    def detect_anomaly(self):
        
        """
        Détecte si trois événements critiques sont survenus en moins de 30 secondes.
        Si c'est le cas, enregistre une alerte.
        """
        critical_events = [e for e in self.events if e.level == "CRITICAL"]
        if len(critical_events) >= 3:
            if (critical_events[-1].timestamp - critical_events[-3].timestamp).total_seconds() <= 30:
                alert = {
                    "time": critical_events[-1].timestamp.isoformat(),
                    "details": "3 événements critiques détectés en moins de 30s"
                }
                if alert not in self.alerts:
                    self.alerts.append(alert)
                    self.save_alerts()

    def save_alerts(self, path="alerts.json"):
        """
        Sauvegarde la liste des alertes dans un fichier JSON.
        
        Parameters
        ----------
        path : str
            Nom du fichier JSON de sortie.
        """
        with open(path, "w") as f:
            json.dump(self.alerts, f, indent=2)

class EventLogger:
    """
    Logger pour enregistrer les traitements dans un fichier système.
    
    Attributs :
    ----------
    logger : logging.Logger
        Instance du logger configuré.
    """
    
    
    def __init__(self, logfile="traceback.log"):
        
        """
        Initialise le logger avec un fichier de sortie.
        
        Parameters
        ----------
        logfile : str
            Nom du fichier log.
        """
        self.logger = logging.getLogger("EventLogger")
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(logfile)
        fh.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        self.logger.addHandler(fh)

    def log(self, msg):
        self.logger.info(msg)


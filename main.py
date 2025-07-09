# Point d'entrée de la CLI


"""
Point d'entrée principal de la CLI du projet de surveillance des événements.

Fonctionnalités :
- Lancer le traitement des logs avec animation spinner et compteur.
- Afficher les alertes détectées.
- Générer un rapport PDF des statistiques et alertes.
- Visualiser un histogramme des niveaux d'événements.
- Quitter proprement.

Utilise asyncio pour la lecture asynchrone des événements.
"""

# main.py
import asyncio
import json
import sys
import itertools
from event import EventAnalyzer, EventLogger,Event
from reader import read_log_file
from reporter import generate_pdf_report
from visualizer import plot_events
from colorama import init, Fore, Style

init(autoreset=True)

analyzer = EventAnalyzer()
logger = EventLogger()




# Spinner animé
async def spinner(task_done_event):
    
    """
    Coroutine affichant un spinner animé pendant que le traitement est en cours.

    Parameters
    ----------
    task_done_event : asyncio.Event
        Événement asyncio qui indique au spinner quand s'arrêter.
    """
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if task_done_event.is_set():
            break
        sys.stdout.write(Fore.YELLOW + f'\r Traitement en cours... {c}')
        sys.stdout.flush()
        await asyncio.sleep(0.1)
    sys.stdout.write(Fore.GREEN + "\r Traitement terminé.            \n")



# Lancer traitement + spinner + compteur
async def launch_processing_with_spinner():
    """
    Lancement du traitement asynchrone avec affichage d'un spinner et compteur
    indiquant le nombre d'événements traités en temps réel.
    """
    task_done_event = asyncio.Event()
    spinner_task = asyncio.create_task(spinner(task_done_event))
    await read_log_file_with_counter(analyzer, logger)
    task_done_event.set()
    await spinner_task


# Lecture du fichier + compteur
    """
    Lecture du fichier 'events.log' ligne par ligne avec un délai simulé de 2 secondes.
    Met à jour un compteur en temps réel du nombre d'événements traités.

    Parameters
    ----------
    analyzer : EventAnalyzer
        Instance qui gère l'ajout d'événements et la détection d'anomalies.
    logger : EventLogger
        Logger pour écrire les traitements dans un fichier système.
    """
async def read_log_file_with_counter(analyzer, logger):
    count = 0
    with open("events.log", "r") as f:
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
            count += 1
            sys.stdout.write(Fore.CYAN + f"\rNombre d'événements traités : {count}")
            sys.stdout.flush()
    print()  # saut de ligne après compteur

 
    
## chargement du fichier log    
async def launch_processing():
    await read_log_file("events.log", analyzer, logger)

def menu():
    """
    Affiche le menu interactif CLI permettant à l'utilisateur :
    - De lancer le traitement avec spinner et compteur.
    - D'afficher les alertes détectées.
    - De générer un rapport PDF avec stats et alertes.
    - De visualiser un histogramme matplotlib.
    - De quitter proprement.
    """
    while True:
            print(Fore.CYAN + "\n--- Menu Surveillance ---")
            print(Fore.YELLOW + "1. Lancer le traitement")
            print(Fore.YELLOW + "2. Afficher alertes")
            print(Fore.YELLOW + "3. Générer rapport")
            print(Fore.YELLOW + "4. Visualiser histogramme")
            print(Fore.YELLOW + "5. Quitter")
            choice = input(Fore.GREEN + "Choisissez une option: ")
            if choice == "1":
                asyncio.run(launch_processing_with_spinner())
            elif choice == "2":
                print(Fore.MAGENTA + json.dumps(analyzer.alerts, indent=2))
            elif choice == "3":
                generate_pdf_report(analyzer)
                print(Fore.BLUE + "Rapport généré dans report.pdf")
            elif choice == "4":
                plot_events(analyzer)
            elif choice == "5":
                print(Fore.RED + "Au revoir ")
                break
            else:
                print(Fore.RED + "Option invalide. Veuillez choisir entre 1 et 5.")
    

if __name__ == "__main__":
    menu()









########################################### ANCIEN MAIN.py ###############################################

# async def launch_processing():
#     await read_log_file("events.log", analyzer, logger)

# def menu():
#     while True:
#         print("\n--- Menu Surveillance ---")
#         print("1. Lancer le traitement")
#         print("2. Afficher alertes")
#         print("3. Générer rapport")
#         print("4. Visualiser histogramme")
#         print("5. Quitter")
#         choice = input("Choisissez une option: ")
#         if choice == "1":
#             asyncio.run(launch_processing())
#         elif choice == "2":
#             print(json.dumps(analyzer.alerts, indent=2))
#         elif choice == "3":
#             generate_pdf_report(analyzer)
#             print("Rapport PDF généré dans report.pdf")
#         elif choice == "4":
#             plot_events(analyzer)
#         elif choice == "5":
#             print("Au revoir")
#             break
#         else:
#             print("Option invalide.")

# if __name__ == "__main__":
#     menu()

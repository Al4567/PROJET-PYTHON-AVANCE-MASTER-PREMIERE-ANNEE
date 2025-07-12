# génération du rapport

"""
Module pour la génération d'un rapport PDF des événements analysés.

Utilise la bibliothèque fpdf pour créer un document structuré
avec les statistiques et les alertes détectées.
"""
from fpdf import FPDF

############################ FONCTION QUI GENERE RAPPORT SOUS FORME DE TEXTE############################
# def generate_report(analyzer, filepath="report.txt"):
#     with open(filepath, "w") as f:
#         f.write(f"Nombre total d'événements: {len(analyzer.events)}\n")
#         f.write(f"Nombre d'événements critiques: {len([e for e in analyzer.events if e.level == 'CRITICAL'])}\n")
#         f.write(f"Nombre d'alertes: {len(analyzer.alerts)}\n\n")
#         f.write("Horodatages des alertes:\n")
#         for alert in analyzer.alerts:
#             f.write(f" - {alert['time']}: {alert['details']}\n")



def generate_pdf_report(analyzer, filepath="report.pdf"):
    
    """
    Génère un rapport PDF résumant :
    - Nombre total d'événements.
    - Nombre d'événements critiques.
    - Nombre et horodatages des alertes.

    Parameters
    ----------
    analyzer : EventAnalyzer
        Instance qui contient les événements et alertes analysés.
    filepath : str
        Nom du fichier PDF généré.
    """
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=14)
    pdf.cell(0, 10, f"Nombre total d'événements: {len(analyzer.events)}", ln=True)
    pdf.cell(0, 10, f"Nombre d'événements critiques: {len([e for e in analyzer.events if e.level == 'CRITICAL'])}", ln=True)
    pdf.cell(0, 10, f"Nombre d'alertes: {len(analyzer.alerts)}", ln=True)
    pdf.ln(10)
    pdf.cell(0, 10, "Horodatages des alertes:", ln=True)
    for alert in analyzer.alerts:
        pdf.cell(0, 10, f" - {alert['time']}: {alert['details']}", ln=True)
    pdf.output(filepath)

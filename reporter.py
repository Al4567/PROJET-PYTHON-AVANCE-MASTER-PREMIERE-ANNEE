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
    
    
    pdf = FPDF(orientation='L', format='A3')  # Paysage A3
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(left=10, top=10, right=10)

    pdf.add_page()

    # Titre principal
    pdf.set_font("Arial", 'B', size=24)
    pdf.cell(0, 20, "Rapport d'Analyse des Événements", ln=True, align='C')
    pdf.ln(10)

    # Résumé global
    pdf.set_font("Arial", size=16)
    pdf.cell(0, 12, f"Nombre total d'événements: {len(analyzer.events)}", ln=True)
    pdf.cell(0, 12, f"Nombre d'événements critiques: {len([e for e in analyzer.events if e.level == 'CRITICAL' or e.level=='ERROR'])}", ln=True)
    pdf.cell(0, 12, f"Nombre total d'alertes: {len(analyzer.alerts)}", ln=True)
    pdf.ln(15)

    # Section alertes
    pdf.set_font("Arial", 'B', size=18)
    pdf.cell(0, 15, "Détails des alertes détectées :", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", size=14)
    if analyzer.alerts:
        for alert in analyzer.alerts:
            alert_text = f"- {alert['time']} : {alert['details']}"
            pdf.multi_cell(0, 10, alert_text)
            pdf.ln(2)
    else:
        pdf.cell(0, 10, "Aucune alerte détectée.", ln=True)

    # Sauvegarde du PDF
    pdf.output(filepath)

    
    
    # pdf = FPDF()
    # pdf = FPDF(orientation='L', format='A3')  # Pour du A3 paysage
    # pdf.add_page()
    # pdf.set_font("Arial", size=14)
    # pdf.cell(0, 10, f"Nombre total d'événements: {len(analyzer.events)}", ln=True)
    # pdf.cell(0, 10, f"Nombre d'événements critiques: {len([e for e in analyzer.events if e.level == 'CRITICAL'])}", ln=True)
    # pdf.cell(0, 10, f"Nombre d'alertes: {len(analyzer.alerts)}", ln=True)
    # pdf.ln(10)
    # pdf.cell(0, 10, "Horodatages des alertes:", ln=True)
    # for alert in analyzer.alerts:
    #     pdf.cell(0, 10, f" - {alert['time']}: {alert['details']}", ln=True)
    # pdf.output(filepath)

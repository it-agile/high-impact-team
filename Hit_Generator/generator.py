import csv
import os

# Ordner für die fertigen Seiten erstellen, falls er nicht existiert
output_ordner = 'generierte_seiten'
if not os.path.exists(output_ordner):
    os.makedirs(output_ordner)

# 1. Template laden
with open('template.html', mode='r', encoding='utf-8') as f:
    template_content = f.read()

# 2. CSV Daten zeilenweise verarbeiten
with open('daten.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for zeile in reader:
        html_output = template_content
        
        # Alle Platzhalter in der aktuellen Zeile ersetzen
        for key, value in zeile.items():
            platzhalter = "{{" + key + "}}"
            html_output = html_output.replace(platzhalter, value)
        
        # Dateiname aus der Spalte 'dateiname' nehmen
        dateiname = f"{zeile['Slug']}.html"
        pfad = os.path.join(output_ordner, dateiname)
        
        # Die fertige Seite speichern
        with open(pfad, mode='w', encoding='utf-8') as f_out:
            f_out.write(html_output)
            print(f"Erstellt: {dateiname}")

print("\nFertig! Alle Seiten befinden sich im Ordner 'generierte_seiten'.")
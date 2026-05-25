import os
import json
from src.parser import parse_asn_file
from src.validator import validate_asn

# 1. Configuration du chemin dynamique
# On récupère le chemin absolu du répertoire où se trouve ce script
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "sample_asn.txt")

# 2. Lecture du fichier source
try:
    with open(file_path, "r") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Erreur : Le fichier {file_path} est introuvable.")
    exit(1)

# 3. Extraction (Parsing)
data = parse_asn_file(content)

# 4. Validation des données
errors = validate_asn(data)

# 5. Affichage du rapport final
print("--- Résultat du Traitement ASN ---")
print(json.dumps(data, indent=4))

print("\n--- Rapport de Validation ---")
if errors:
    print(f"⚠️ {len(errors)} erreur(s) détectée(s) :")
    for error in errors:
        print(f" - {error}")
else:
    print("✅ Données conformes, aucune erreur détectée.")
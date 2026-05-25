# Inbound ASN Validator

## 🚀 Présentation
Cet outil est un pipeline de traitement de données conçu pour valider les avis d'expédition (ASN - Advanced Shipping Notice) dans un contexte de Supply Chain. Il transforme des données textuelles brutes en objets structurés et applique des règles métiers strictes pour assurer la conformité des expéditions.

## 🛠 Architecture du projet
Le projet suit une structure modulaire pour garantir la maintenabilité et la scalabilité :
- `src/` : Contient la logique métier (`parser.py` pour l'extraction, `validator.py` pour le contrôle qualité).
- `tests/` : Suite de tests unitaires utilisant `pytest` pour garantir la robustesse du code.
- `app.py` : Interface utilisateur interactive développée avec **Streamlit**.
- `run_parser.py` : Script d'exécution en ligne de commande pour le traitement local.

## ⚙️ Installation
1. Cloner le dépôt : `git clone https://github.com/sbadji/inbound-asn-validator.git`
2. Créer un environnement virtuel : `python -m venv venv`
3. Activer l'environnement : `source venv/bin/activate`
4. Installer les dépendances : `pip install -r requirements.txt` (Pense à générer ce fichier avec `pip freeze > requirements.txt`)

## 💡 Utilisation
- **Via CLI** : `python run_parser.py`
- **Via Interface Web** : `streamlit run app.py`

## 🎯 Intention
Ce projet a été réalisé dans le but de démontrer une maîtrise du cycle complet de développement (Software Development Life Cycle) : du parsing de données à la mise en place de tests automatisés, jusqu'à l'industrialisation sous forme d'application web.
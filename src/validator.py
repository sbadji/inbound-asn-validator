def validate_asn(data):
    """
    Valide les données extraites selon les règles métiers.
    Algorithme :
    1. Vérifie la présence du supplier_id.
    2. Vérifie chaque ligne de packaging (Type de boîte, Quantité > 0).
    3. Retourne une liste d'erreurs (ou vide si tout est OK).
    """
    errors = []
    
    # Règle 1 : Fournisseur obligatoire
    if not data.get("supplier_id"):
        errors.append("Missing SUPPLIER_ID")
        
    # Règle 2 : Validation des lignes de packaging
    valid_box_types = ["KLT-4314", "GALIA_A12"]
    
    for i, line in enumerate(data.get("packaging_lines", [])):
        # Vérification du type de boîte
        if line["box_type"] not in valid_box_types:
            errors.append(f"Line {i+1}: Invalid box type '{line['box_type']}'")
        
        # Vérification de la quantité
        if line["qty"] <= 0:
            errors.append(f"Line {i+1}: Qty must be > 0")
            
    return errors
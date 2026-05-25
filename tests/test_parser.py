from src.parser import parse_asn_file

def test_parser_extraction():
    sample = "SUPPLIER_ID: TEST_123\nDESADV_REF: BL-001\n[PACKAGING_LINE_01]\nBOX_TYPE: KLT-4314\nQTY: 10\nPART_FAMILY: TEST"
    data = parse_asn_file(sample)
    assert data["supplier_id"] == "TEST_123"
    assert len(data["packaging_lines"]) == 1
    assert data["packaging_lines"][0]["qty"] == 10
def test_parser_with_valid_data():
    """Vérifie que le parser extrait correctement les données d'un ASN valide."""
    sample = (
        "SUPPLIER_ID: SNRA_FR_94821\n"
        "DESADV_REF: BL-2026-X992A\n"
        "[PACKAGING_LINE_01]\n"
        "BOX_TYPE: KLT-4314\n"
        "QTY: 120\n"
        "PART_FAMILY: INJECTION_PLASTIC"
    )
    result = parse_asn_file(sample)
    
    assert result["supplier_id"] == "SNRA_FR_94821"
    assert result["desadv_ref"] == "BL-2026-X992A"
    assert len(result["packaging_lines"]) == 1
    assert result["packaging_lines"][0]["box_type"] == "KLT-4314"
    assert result["packaging_lines"][0]["qty"] == 120

def test_parser_with_empty_content():
    """Vérifie que le parser ne plante pas sur un contenu vide."""
    result = parse_asn_file("")
    assert result["supplier_id"] is None
    assert result["packaging_lines"] == []

def test_parser_with_malformed_data():
    """Vérifie que le parser gère les données mal formées sans planter."""
    sample = "SUPPLIER_ID: SNRA_FR_94821\nDESADV_REF: BL-2026-X992A\n[PACKAGING_LINE_01]\nBOX_TYPE: KLT-4314\nQTY: not_a_number\nPART_FAMILY: INJECTION_PLASTIC"
    result = parse_asn_file(sample)
    
    assert result["supplier_id"] == "SNRA_FR_94821"
    assert result["desadv_ref"] == "BL-2026-X992A"
    assert len(result["packaging_lines"]) == 1
    assert result["packaging_lines"][0]["box_type"] == "KLT-4314"
    # La quantité mal formée doit être traitée comme 0 ou ignorée selon l'implémentation
    assert result["packaging_lines"][0]["qty"] == 0
def test_parser_with_multiple_packaging_lines():
    """Vérifie que le parser peut gérer plusieurs lignes de packaging."""
    sample = (
        "SUPPLIER_ID: SNRA_FR_94821\n"
        "DESADV_REF: BL-2026-X992A\n"
        "[PACKAGING_LINE_01]\n"
        "BOX_TYPE: KLT-4314\n"
        "QTY: 120\n"
        "PART_FAMILY: INJECTION_PLASTIC\n"
        "[PACKAGING_LINE_02]\n"
        "BOX_TYPE: GALIA_A12\n"
        "QTY: 50\n"
        "PART_FAMILY: INJECTION_PLASTIC"
    )
    result = parse_asn_file(sample)
    
    assert result["supplier_id"] == "SNRA_FR_94821"
    assert result["desadv_ref"] == "BL-2026-X992A"
    assert len(result["packaging_lines"]) == 2
    assert result["packaging_lines"][0]["box_type"] == "KLT-4314"
    assert result["packaging_lines"][0]["qty"] == 120
    assert result["packaging_lines"][1]["box_type"] == "GALIA_A12"
    assert result["packaging_lines"][1]["qty"] == 50
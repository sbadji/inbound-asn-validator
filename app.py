import streamlit as st
import json
from src.parser import parse_asn_file
from src.validator import validate_asn

st.title("📦 Inbound ASN Validator")
st.write("Uploadez votre fichier ASN pour vérifier sa conformité.")

uploaded_file = st.file_uploader("Choisir un fichier ASN", type="txt")

if uploaded_file is not None:
    # Lecture du contenu
    content = uploaded_file.getvalue().decode("utf-8")
    
    # Traitement
    data = parse_asn_file(content)
    errors = validate_asn(data)
    
    # Affichage
    st.subheader("Données extraites :")
    st.json(data)
    
    if errors:
        st.error(f"⚠️ {len(errors)} erreur(s) détectée(s) :")
        for error in errors:
            st.write(f"- {error}")
    else:
        st.success("✅ Données conformes !")
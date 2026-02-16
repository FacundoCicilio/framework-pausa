import streamlit as st
import requests

# --------------------------------
# Función para consultar HuggingFace
# --------------------------------
def analizar_con_ia_hf(texto):
    """
    Usa modelo gpt2 de Hugging Face
    para analizar el texto de usuario.
    """
    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {''}"}  # no hace falta API key (nivel gratuito)

    payload = {
        "inputs": f"Analizá esta situación y respondé en lenguaje claro:\n{texto}"
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=20)
    if not response.ok:
        return "No se pudo analizar con la IA (HuggingFace)."

    # El resultado viene como lista de generados
    # Tomamos el texto generado
    data = response.json()
    if isinstance(data, list) and "generated_text" in data[0]:
        return data[0]["generated_text"]
    else:
        return str(data)

# --------------------------------
# Streamlit (parte IA)
# --------------------------------

st.title("💡 P.A.U.S.A. con IA gratuita (HuggingFace)")

idea = st.text_area("Escribí tu idea:", "")

if st.button("Analizar con IA gratuita"):
    if idea.strip() == "":
        st.error("Escribí algo primero.")
    else:
        with st.spinner("Analizando con IA gratuita..."):
            respuesta = analizar_con_ia_hf(idea)
            st.markdown(respuesta)

import streamlit as st
from openai import OpenAI

# ---------------------
# CONFIGURACIÓN
# ---------------------
st.set_page_config(page_title="💡 P.A.U.S.A. IA", page_icon="🧠", layout="centered")

st.title("💡 P.A.U.S.A. – Decisiones bajo presión (IA)")
st.markdown("La IA analiza tu situación y te ayuda a reflexionar antes de actuar.")
st.divider()

# ⚠️ Poné tu API key en Streamlit secrets o directamente acá
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------------------
# FORMULARIO
# ---------------------
with st.form("form_pausa"):
    idea = st.text_area("Escribí tu idea o lo que querés hacer:", "", height=120)
    impulso = st.checkbox("Esto surge por impulso")
    riesgo = st.checkbox("Podría afectar a alguien o generar problemas")
    apoyo = st.slider("¿Qué tan probable es que otros apoyen tu acción?", 0.0, 1.0, 0.5, 0.05)

    submit = st.form_submit_button("🔎 Analizar con IA")

# ---------------------
# PROCESAMIENTO
# ---------------------
if submit and idea:

    st.divider()
    st.markdown("## Análisis IA")

    # Prompt profesional y seguro
    prompt = f"""
    Analizá la siguiente situación de manera didáctica y prudente.

    Texto del usuario:
    "{idea}"

    Indicadores:
    - Surge por impulso: {impulso}
    - Puede afectar a alguien: {riesgo}
    - Nivel de apoyo percibido: {apoyo}

    Tareas:
    1. Detectar si hay impulsividad o riesgo.
    2. Explicar brevemente posibles consecuencias.
    3. Dar una recomendación prudente y clara.
    4. Sugerir un primer paso pequeño y seguro.

    Responder en tono claro, simple y responsable.
    No dar consejos médicos, legales ni financieros específicos.
    """

    with st.spinner("Analizando..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Sos un orientador cognitivo prudente y didáctico."},
                {"role": "user", "content": prompt}
            ]
        )

    respuesta_ia = response.choices[0].message.content

    st.markdown(respuesta_ia)

# ---------------------
# NOTA LEGAL
# ---------------------
st.divider()
st.warning("""
⚠️ Esta herramienta usa inteligencia artificial para generar reflexiones orientativas.
No constituye asesoramiento profesional de ningún tipo.
La decisión final siempre es responsabilidad del usuario.
""")

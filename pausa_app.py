import streamlit as st
import requests
from datetime import datetime

# ---------------------
# Configuración
# ---------------------
st.set_page_config(page_title="💡 P.A.U.S.A. PRO", page_icon="🧠", layout="centered")

st.title("💡 P.A.U.S.A. – Decisiones bajo presión")
st.markdown("Un modelo reflexivo basado en probabilidad y análisis estratégico para ayudarte a frenar el impulso y decidir con claridad.")
st.divider()

# ---------------------
# FUNCIÓN DIDÁCTICA (LLM como capa explicativa)
# ---------------------
def generar_interpretacion(idea, p_exito, nivel, impulso, riesgo, apoyo):

    contexto = f"""
Situación del usuario:
{idea}

Probabilidad estimada de resultado favorable: {int(p_exito*100)}%
Nivel calculado: {nivel}
Impulso detectado: {impulso}
Riesgo potencial: {riesgo}
Nivel de apoyo: {apoyo}

Redactá una interpretación clara, breve y reflexiva alineada con un análisis de probabilidad y teoría de juegos.
No menciones modelos matemáticos ni IA.
Explicá qué significa el resultado y qué actitud estratégica conviene adoptar.
"""

    API_URL = "https://api-inference.huggingface.co/models/gpt2"

    payload = {"inputs": contexto}

    try:
        response = requests.post(API_URL, json=payload, timeout=20)
        data = response.json()

        if isinstance(data, list) and "generated_text" in data[0]:
            texto = data[0]["generated_text"]
            return texto.replace(contexto, "").strip()
        else:
            return "El análisis sugiere actuar con prudencia y evaluar las consecuencias estratégicas antes de avanzar."

    except:
        return "El análisis sugiere actuar con prudencia y evaluar las consecuencias estratégicas antes de avanzar."


# ---------------------
# FORMULARIO PRINCIPAL
# ---------------------
with st.form("form_pausa"):

    st.markdown("### Tu situación")
    idea = st.text_area("Escribí tu idea o lo que querés hacer:", "", height=100)

    impulso = st.checkbox("Esto surge por impulso")
    riesgo = st.checkbox("Podría afectar a alguien o generar problemas")
    apoyo = st.slider(
        "¿Qué tan probable es que otros apoyen tu acción?",
        0.0, 1.0, 0.5, 0.05
    )

    submit = st.form_submit_button("🔎 Evaluar decisión")

# ---------------------
# RESULTADOS
# ---------------------
if submit:

    # ---------------------
    # MODELO BAYES SIMPLIFICADO
    # ---------------------
    p_exito_base = 0.6

    penalizacion = 0
    if impulso:
        penalizacion += 0.2
    if riesgo:
        penalizacion += 0.3

    bonus_apoyo = 0.25 * apoyo

    p_exito = p_exito_base - penalizacion + bonus_apoyo
    p_exito = min(max(p_exito, 0.1), 0.9)

    # ---------------------
    # NIVEL ESTRATÉGICO
    # ---------------------
    if p_exito < 0.35:
        nivel = "Riesgo Alto"
        recomendacion = "Conviene no actuar ahora. Replanteá la estrategia."
    elif p_exito < 0.6:
        nivel = "Precaución"
        recomendacion = "Avanzá solo con un paso pequeño y reversible."
    else:
        nivel = "Condiciones Favorables"
        recomendacion = "Podés avanzar, manteniendo prudencia."

    # ---------------------
    # MOSTRAR RESULTADOS
    # ---------------------
    st.divider()
    st.markdown("## Resultado del análisis estratégico")

    st.metric("Probabilidad estimada de resultado favorable", f"{int(p_exito*100)}%")
    st.progress(p_exito)

    st.markdown(f"### {nivel}")
    st.markdown(f"**{recomendacion}**")

    # ---------------------
    # INTERPRETACIÓN DIDÁCTICA
    # ---------------------
    st.markdown("### Interpretación reflexiva")

    explicacion_basica = []

    if impulso:
        explicacion_basica.append("La decisión presenta señales de impulso.")
    if riesgo:
        explicacion_basica.append("Existen posibles consecuencias negativas para terceros.")
    if apoyo < 0.4:
        explicacion_basica.append("El apoyo externo es bajo, lo que reduce estabilidad estratégica.")
    elif apoyo > 0.7:
        explicacion_basica.append("El apoyo externo es sólido, lo que mejora la posición estratégica.")

    if not explicacion_basica:
        explicacion_basica.append("No se detectan factores críticos inmediatos.")

    for e in explicacion_basica:
        st.write("•", e)

    # Interpretación ampliada (didáctica)
    with st.spinner("Generando análisis reflexivo..."):
        interpretacion = generar_interpretacion(
            idea, p_exito, nivel, impulso, riesgo, apoyo
        )

    st.markdown(interpretacion)

    # ---------------------
    # PRIMER PASO PRUDENTE
    # ---------------------
    st.markdown("### Definí tu próximo paso prudente")

    with st.form("form_accion"):
        accion = st.text_input("¿Cuál es el paso más pequeño y seguro que podrías hacer ahora?")
        confirmar_accion = st.form_submit_button("Confirmar paso estratégico")

    if confirmar_accion and accion:
        st.success(f"✔ Paso definido: {accion}")
        st.info("Sugerencia: realizalo pronto para evitar que el impulso vuelva a dominar la decisión.")

# ---------------------
# NOTA FINAL
# ---------------------
st.divider()
st.warning("""
Esta herramienta es un modelo simplificado con fines reflexivos y educativos.
No constituye asesoramiento legal, médico, financiero ni psicológico.
La decisión final siempre es responsabilidad del usuario.
""")

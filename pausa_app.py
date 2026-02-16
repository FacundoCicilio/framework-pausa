import streamlit as st
from datetime import datetime

# -------------------------------------------------
# CONFIGURACIÓN
# -------------------------------------------------
st.set_page_config(
    page_title="💡 P.A.U.S.A. Minimalista",
    page_icon="⚡",
    layout="centered"
)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.title("💡 P.A.U.S.A. Minimalista")
st.markdown("""
Tomar decisiones bajo presión puede generar errores.  
Este mini-framework te ayuda a frenar el impulso y evaluar rápidamente.
""")
st.divider()

# -------------------------------------------------
# INPUTS CLAVE
# -------------------------------------------------
st.markdown("### Captura tu idea (opcional)")
idea = st.text_area("Idea breve:", "", height=80)

st.markdown("### Evaluá tu situación rápidamente")
impulso = st.checkbox("Siento que esto surge por impulso")
riesgo = st.checkbox("Podría afectar a alguien o generar problemas")
apoyo = st.slider("Probabilidad de que otros apoyen tu acción", 0.0, 1.0, 0.5, 0.05)

# -------------------------------------------------
# SCORE Y RECOMENDACIÓN
# -------------------------------------------------
# Calculamos score simple
score_alerta = sum([impulso, riesgo])  # 0, 1, 2

# Ajustamos según apoyo social
if apoyo > 0.7:
    score_alerta -= 0.5
elif apoyo < 0.3:
    score_alerta += 0.5

# Recomendación simple
if score_alerta <= 0.5:
    recomendacion = "🟢 Avanzar con precaución"
elif score_alerta <= 1.5:
    recomendacion = "🟡 Pausa breve y pensá 5-10 min"
else:
    recomendacion = "🔴 Replanificar antes de actuar"

st.markdown("### Recomendación inmediata")
st.markdown(f"**{recomendacion}**", unsafe_allow_html=True)

# -------------------------------------------------
# ACCIÓN MÍNIMA SEGURA
# -------------------------------------------------
if recomendacion == "🟢 Avanzar con precaución":
    accion = st.text_input("Definí tu acción mínima segura (opcional)")
    if accion:
        st.info(f"💡 Acción mínima segura: {accion}")

# -------------------------------------------------
# REGISTRO OPCIONAL
# -------------------------------------------------
if st.button("Registrar idea y decisión"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.success(f"Idea registrada a las {timestamp}")
    st.code(f"""
Idea: {idea}
Impulso: {impulso}
Riesgo: {riesgo}
Apoyo social: {apoyo}
Score alerta: {score_alerta:.1f}
Recomendación: {recomendacion}
Acción mínima segura: {accion if recomendacion == "🟢 Avanzar con precaución" else "N/A"}
Fecha: {timestamp}
""")

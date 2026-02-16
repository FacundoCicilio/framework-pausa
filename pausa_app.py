import streamlit as st
from datetime import datetime

# ----------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ----------------------------
st.set_page_config(
    page_title="Framework P.A.U.S.A.",
    page_icon="🧠",
    layout="centered"
)

# ----------------------------
# HEADER
# ----------------------------
st.title("🧠 Framework P.A.U.S.A.")
st.subheader("Protocolo Algorítmico de Urgencias Sociales y Acción")
st.markdown(
    """
    **Objetivo:** Reducir errores bajo presión social o impulso.  
    Respondé con honestidad. Tarda menos de 30 segundos.
    """
)

st.divider()

# ----------------------------
# PREGUNTAS
# ----------------------------

st.markdown("### Evaluación de la situación")

presion = st.checkbox("1️⃣ ¿Estoy siendo apurado por alguien?")
riesgo = st.checkbox("2️⃣ ¿Hay riesgo legal o estoy usando algo que no es mío?")
exposicion = st.checkbox("3️⃣ ¿Me incomodaría que me filmen haciendo esto?")
identidad = st.checkbox("4️⃣ ¿Esto NO es coherente con quien quiero ser?")
urgencia = st.checkbox("5️⃣ ¿No es realmente urgente decidir ahora?")

st.divider()

# ----------------------------
# EVALUACIÓN
# ----------------------------

if st.button("🔎 Evaluar decisión"):

    riesgo_score = sum([presion, riesgo, exposicion, identidad, urgencia])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    st.markdown("## Resultado")

    # Regla principal
    if riesgo_score >= 2:
        st.error("🔴 RECOMENDACIÓN: NO AVANZAR")
        st.markdown("Tomá distancia. Replanteá la decisión.")
    elif riesgo_score == 1:
        st.warning("🟡 RECOMENDACIÓN: PAUSA 10 MINUTOS")
        st.markdown("Dale tiempo al sistema racional.")
    else:
        st.success("🟢 RECOMENDACIÓN: OK PARA AVANZAR")
        st.markdown("La decisión parece alineada y sin presión significativa.")

    st.markdown(f"**Score de alerta:** {riesgo_score} / 5")
    st.caption(f"Evaluado el: {timestamp}")

st.divider()

# ----------------------------
# FOOTER CONCEPTUAL
# ----------------------------
st.markdown(
    """
    ---
    ### 📌 Principio central
    
    > La mayoría de los errores no provienen de falta de inteligencia,  
    > sino de decisiones tomadas bajo presión social y urgencia artificial.
    
    Framework diseñado para reducir decisiones impulsivas.
    """
)
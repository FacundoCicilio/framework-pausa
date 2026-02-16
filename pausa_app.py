import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Framework P.A.U.S.A.",
    page_icon="🧠",
    layout="centered"
)

# ----------------------------
# ESTILO SIMPLE MÁS LIMPIO
# ----------------------------

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
.result-box {
    padding: 1.5rem;
    border-radius: 12px;
    background-color: #f5f7fa;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# HEADER
# ----------------------------

st.title("🧠 Framework P.A.U.S.A.")
st.markdown("### De impulso a estrategia en 30 segundos")

st.markdown("""
Tomar decisiones bajo presión suele generar errores evitables.  
Este framework te ayuda a frenar el impulso y pensar mejor.
""")

st.divider()

# ----------------------------
# EVALUACIÓN
# ----------------------------

st.markdown("## 📝 Evaluación rápida")

presion = st.checkbox("¿Estoy siendo apurado por alguien?")
st.caption("La presión externa reduce claridad.")

riesgo = st.checkbox("¿Hay riesgo legal o estoy usando algo que no es mío?")
st.caption("Si hay consecuencias formales posibles, atención.")

exposicion = st.checkbox("¿Me incomodaría que me filmen haciendo esto?")
st.caption("Pensá en tu yo futuro.")

identidad = st.checkbox("¿Esto NO es coherente con quien quiero ser?")
st.caption("Las decisiones pequeñas construyen identidad.")

urgencia = st.checkbox("¿No es realmente urgente decidir ahora?")
st.caption("La urgencia artificial es una trampa común.")

riesgo_score = sum([presion, riesgo, exposicion, identidad, urgencia])

st.divider()

# ----------------------------
# RESULTADO
# ----------------------------

st.markdown("## 📊 Resultado")

if riesgo_score == 0:
    st.info("👋 Marcá al menos una casilla para activar el análisis.")
else:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    st.markdown(f"### Score de alerta: **{riesgo_score} / 5**")

    if riesgo_score >= 2:
        st.error("🔴 Recomendación: NO AVANZAR")
        st.write("Tomá distancia. Replanteá la decisión.")
    elif riesgo_score == 1:
        st.warning("🟡 Recomendación: PAUSA 10 MINUTOS")
        st.write("Dale tiempo al sistema racional.")
    else:
        st.success("🟢 Recomendación: OK PARA AVANZAR")
        st.write("No se detectan alertas significativas.")

    st.caption(f"Evaluado el: {timestamp}")

    st.divider()

    # ----------------------------
    # MODO PROBABILIDAD
    # ----------------------------

    st.markdown("## 🔮 Modo Probabilidad (opcional)")

    activar_bayes = st.checkbox("Quiero estimar la probabilidad de que salga mal")

    if activar_bayes:

        prior = st.slider(
            "En general, ¿qué tan seguido este tipo de decisiones te salen mal? (%)",
            0, 100, 20
        ) / 100

        evidencia = st.slider(
            "En este caso puntual, ¿qué tan fuerte sentís la alerta? (%)",
            0, 100, riesgo_score * 20
        ) / 100

        posterior = (prior * evidencia) / (
            (prior * evidencia) + ((1 - prior) * (1 - evidencia))
        )

        st.markdown("### 📈 Estimación ajustada")

        st.write(
            f"Probabilidad estimada de que esta decisión salga mal: **{round(posterior*100,1)}%**"
        )

        if posterior > 0.6:
            st.error("Alta probabilidad. No parece buena idea.")
        elif posterior > 0.3:
            st.warning("Riesgo moderado. Quizás conviene pausar.")
        else:
            st.success("Riesgo bajo según tu estimación.")

st.divider()

# ----------------------------
# IDEA CENTRAL
# ----------------------------

st.markdown("## 📌 Idea central")

st.markdown("""
La mayoría de los errores no vienen de falta de inteligencia.  
Vienen de decisiones tomadas bajo presión social y urgencia artificial.  

Este es solo un pequeño freno racional antes del impulso.
""")

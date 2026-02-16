import streamlit as st
from datetime import datetime

# -------------------------------------------------
# CONFIGURACIÓN
# -------------------------------------------------

st.set_page_config(
    page_title="Framework P.A.U.S.A.",
    page_icon="🧠",
    layout="centered"
)

# -------------------------------------------------
# ESTILO SUTIL
# -------------------------------------------------

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
.section-title {
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.title("🧠 Framework P.A.U.S.A.")
st.markdown("### De impulso a estrategia en menos de 30 segundos")

st.markdown("""
Tomar decisiones bajo presión suele generar errores evitables.  
Este pequeño motor te ayuda a frenar el impulso y pensar mejor.
""")

st.divider()

# -------------------------------------------------
# EVALUACIÓN
# -------------------------------------------------

st.markdown("## 📝 Evaluación rápida")
st.markdown("Marcá lo que aplique en tu situación actual:")

presion = st.checkbox("¿Estoy siendo apurado por alguien?")
st.caption("La presión externa reduce claridad mental.")

riesgo = st.checkbox("¿Hay riesgo legal o estoy usando algo que no es mío?")
st.caption("Si hay consecuencias formales posibles, atención.")

exposicion = st.checkbox("¿Me incomodaría que me filmen haciendo esto?")
st.caption("Pensá en tu versión futura viendo esta decisión.")

identidad = st.checkbox("¿Esto NO es coherente con quien quiero ser?")
st.caption("Las decisiones pequeñas construyen identidad.")

urgencia = st.checkbox("¿No es realmente urgente decidir ahora?")
st.caption("La urgencia artificial suele generar errores.")

riesgo_score = sum([presion, riesgo, exposicion, identidad, urgencia])

st.divider()

# -------------------------------------------------
# RESULTADO
# -------------------------------------------------

st.markdown("## 📊 Resultado")

if riesgo_score == 0:
    st.info("👋 Marcá al menos una casilla para activar el análisis.")
else:

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Score visible
    st.markdown(f"### Score de alerta: **{riesgo_score} / 5**")

    # Barra visual
    st.progress(riesgo_score / 5)

    # Nivel textual
    if riesgo_score <= 1:
        nivel = "🟢 Riesgo Bajo"
    elif riesgo_score == 2:
        nivel = "🟡 Riesgo Moderado"
    else:
        nivel = "🔴 Riesgo Alto"

    st.markdown(f"**Nivel estimado:** {nivel}")

    st.divider()

    # Recomendación principal
    if riesgo_score >= 3:
        st.error("🔴 Recomendación: NO AVANZAR")
        st.write("Tomá distancia. Replanteá la decisión con mayor claridad.")
    elif riesgo_score == 2:
        st.warning("🟡 Recomendación: PAUSA 10 MINUTOS")
        st.write("Dale tiempo al sistema racional antes de actuar.")
    else:
        st.success("🟢 Recomendación: OK PARA AVANZAR")
        st.write("No se detectan alertas significativas.")

    st.caption(f"Evaluado el: {timestamp}")

    st.divider()

    # -------------------------------------------------
    # MODO PROBABILIDAD
    # -------------------------------------------------

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

        prob = round(posterior * 100, 1)
        st.markdown(f"Probabilidad estimada de que salga mal: **{prob}%**")

        if posterior > 0.6:
            st.error("Alta probabilidad. No parece buena idea.")
        elif posterior > 0.3:
            st.warning("Riesgo moderado. Quizás conviene pausar.")
        else:
            st.success("Riesgo bajo según tu estimación.")

st.divider()

# -------------------------------------------------
# IDEA CENTRAL
# -------------------------------------------------

st.markdown("## 📌 Idea central")

st.markdown("""
La mayoría de los errores no vienen de falta de inteligencia.  
Vienen de decisiones tomadas bajo presión social y urgencia artificial.  

Esto no reemplaza tu criterio.  
Solo introduce una pausa racional antes del impulso.
""")

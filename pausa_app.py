import streamlit as st
from datetime import datetime

# -------------------------------------------------
# CONFIGURACIÓN
# -------------------------------------------------

st.set_page_config(
    page_title="P.A.U.S.A. Protocol",
    page_icon="🧠",
    layout="centered"
)

# -------------------------------------------------
# ESTILO
# -------------------------------------------------

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
.version-tag {
    color: gray;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER IDENTIDAD
# -------------------------------------------------

st.title("🧠 P.A.U.S.A.")
st.markdown("### Presión – Apuro – Urgencia – Señal – Acción")

st.markdown('<div class="version-tag">v1.0 — Motor básico de decisión bajo presión</div>', unsafe_allow_html=True)

st.markdown("""
Un micro-sistema para reducir errores cuando la presión social,
la urgencia o el impulso intentan decidir por vos.
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
    st.info("Marcá al menos una casilla para activar el análisis.")
else:

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    st.markdown(f"### Score de alerta: **{riesgo_score} / 5**")
    st.progress(riesgo_score / 5)

    if riesgo_score <= 1:
        nivel = "🟢 Riesgo Bajo"
    elif riesgo_score == 2:
        nivel = "🟡 Riesgo Moderado"
    else:
        nivel = "🔴 Riesgo Alto"

    st.markdown(f"**Nivel estimado:** {nivel}")

    st.divider()

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
# MANIFIESTO
# -------------------------------------------------

st.markdown("## 📌 Manifiesto")

st.markdown("""
La mayoría de los errores no vienen de falta de inteligencia.  
Vienen de decisiones tomadas bajo presión social y urgencia artificial.

P.A.U.S.A. no reemplaza tu criterio.  
Introduce un espacio racional entre el impulso y la acción.
""")

st.divider()

# -------------------------------------------------
# ROADMAP
# -------------------------------------------------

st.markdown("## 🚀 Próximas versiones")

st.markdown("""
- Historial anónimo de decisiones  
- Perfil personal de riesgo  
- Consejos dinámicos según patrón  
- Dashboard de autocontrol  
- Versiones temáticas (legal, relaciones, inversiones)
""")

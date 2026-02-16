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
# HEADER
# -------------------------------------------------

st.title("🧠 Framework P.A.U.S.A.")
st.markdown("## Protocolo Algorítmico de Urgencias Sociales y Acción")

st.markdown("""
Tomar decisiones bajo presión suele generar errores evitables.  
Este framework te ayuda a frenar el impulso y pensar mejor.  
⏱ Tarda menos de 30 segundos.
""")

st.divider()

# -------------------------------------------------
# EVALUACIÓN
# -------------------------------------------------

st.markdown("# 📝 Evaluación rápida")

st.markdown("Marcá lo que aplique en tu situación actual:")

presion = st.checkbox("1️⃣ ¿Estoy siendo apurado por alguien?")
st.caption("Presión externa suele nublar el criterio.")

riesgo = st.checkbox("2️⃣ ¿Hay riesgo legal o estoy usando algo que no es mío?")
st.caption("Si hay consecuencias formales posibles, atención.")

exposicion = st.checkbox("3️⃣ ¿Me incomodaría que me filmen haciendo esto?")
st.caption("Buena prueba de coherencia futura.")

identidad = st.checkbox("4️⃣ ¿Esto NO es coherente con quien quiero ser?")
st.caption("Decisiones pequeñas construyen identidad.")

urgencia = st.checkbox("5️⃣ ¿No es realmente urgente decidir ahora?")
st.caption("La urgencia artificial es un clásico generador de errores.")

# -------------------------------------------------
# CÁLCULO
# -------------------------------------------------

riesgo_score = sum([presion, riesgo, exposicion, identidad, urgencia])
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.divider()

st.markdown("# 📊 Resultado")

# Score visible primero
st.markdown(f"### Score de alerta: **{riesgo_score} / 5**")

if riesgo_score >= 2:
    st.error("🔴 Recomendación: NO AVANZAR")
    st.markdown("Tomá distancia. Replanteá la decisión.")
elif riesgo_score == 1:
    st.warning("🟡 Recomendación: PAUSA 10 MINUTOS")
    st.markdown("Dale tiempo al sistema racional.")
else:
    st.success("🟢 Recomendación: OK PARA AVANZAR")
    st.markdown("No se detectan alertas significativas.")

st.caption(f"Evaluado el: {timestamp}")

st.divider()

# -------------------------------------------------
# MODO PROBABILIDAD
# -------------------------------------------------

st.markdown("# 🔮 Modo Probabilidad (opcional y curioso)")

st.markdown("""
Si querés ir un paso más allá, podés estimar la probabilidad
de que esta decisión salga mal usando tu experiencia previa.
""")

activar_bayes = st.checkbox("Quiero estimar la probabilidad")

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
        st.error("🚨 Alta probabilidad. No parece buena idea.")
    elif posterior > 0.3:
        st.warning("⚠️ Riesgo moderado. Quizás conviene pausar.")
    else:
        st.success("✅ Riesgo bajo según tu propia estimación.")

st.divider()

# -------------------------------------------------
# IDEA CENTRAL
# -------------------------------------------------

st.markdown("# 📌 Idea central")

st.markdown("""
La mayoría de los errores no vienen de falta de inteligencia.  
Vienen de decisiones tomadas bajo presión social y urgencia artificial.  

Este es solo un pequeño freno racional antes del impulso.
""")

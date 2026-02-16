import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Framework P.A.U.S.A.",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Framework P.A.U.S.A.")
st.subheader("Protocolo Algorítmico de Urgencias Sociales y Acción")

st.markdown("""
Tomar decisiones bajo presión suele generar errores evitables.  
Este framework te ayuda a frenar el impulso y pensar mejor.  
Tarda menos de 30 segundos.
""")

st.divider()

# ----------------------------
# CHECKLIST
# ----------------------------

st.markdown("### Evaluación rápida")

presion = st.checkbox("1️⃣ ¿Estoy siendo apurado por alguien?")
riesgo = st.checkbox("2️⃣ ¿Hay riesgo legal o estoy usando algo que no es mío?")
exposicion = st.checkbox("3️⃣ ¿Me incomodaría que me filmen haciendo esto?")
identidad = st.checkbox("4️⃣ ¿Esto NO es coherente con quien quiero ser?")
urgencia = st.checkbox("5️⃣ ¿No es realmente urgente decidir ahora?")

# ----------------------------
# CÁLCULO AUTOMÁTICO
# ----------------------------

riesgo_score = sum([presion, riesgo, exposicion, identidad, urgencia])
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.divider()
st.markdown("## Resultado")

if riesgo_score >= 2:
    st.error("🔴 Recomendación: NO AVANZAR")
    st.markdown("Tomá distancia. Replanteá la decisión.")
elif riesgo_score == 1:
    st.warning("🟡 Recomendación: PAUSA 10 MINUTOS")
    st.markdown("Dale tiempo al sistema racional.")
else:
    st.success("🟢 Recomendación: OK PARA AVANZAR")
    st.markdown("No se detectan alertas significativas.")

st.markdown(f"**Score de alerta:** {riesgo_score} / 5")
st.caption(f"Evaluado el: {timestamp}")

st.divider()

# ----------------------------
# MODO PROBABILIDAD
# ----------------------------

st.markdown("### 🔮 Modo Probabilidad (opcional y curioso)")
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

    st.markdown("### 📊 Estimación ajustada")

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

st.markdown("""
### 📌 Idea central

La mayoría de los errores no vienen de falta de inteligencia.  
Vienen de decisiones tomadas bajo presión social y urgencia artificial.  

Este es solo un pequeño freno racional antes del impulso.
""")

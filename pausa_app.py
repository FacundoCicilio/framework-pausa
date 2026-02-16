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
**Objetivo:** Reducir errores bajo presión social o impulso.  
Respondé con honestidad. Tarda menos de 30 segundos.
""")

st.divider()

st.markdown("### Evaluación de la situación")

presion = st.checkbox("1️⃣ ¿Estoy siendo apurado por alguien?")
riesgo = st.checkbox("2️⃣ ¿Hay riesgo legal o estoy usando algo que no es mío?")
exposicion = st.checkbox("3️⃣ ¿Me incomodaría que me filmen haciendo esto?")
identidad = st.checkbox("4️⃣ ¿Esto NO es coherente con quien quiero ser?")
urgencia = st.checkbox("5️⃣ ¿No es realmente urgente decidir ahora?")

st.divider()

if st.button("🔎 Evaluar decisión"):

    riesgo_score = sum([presion, riesgo, exposicion, identidad, urgencia])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    st.markdown("## Resultado")

    if riesgo_score >= 2:
        st.error("🔴 RECOMENDACIÓN: NO AVANZAR")
    elif riesgo_score == 1:
        st.warning("🟡 RECOMENDACIÓN: PAUSA 10 MINUTOS")
    else:
        st.success("🟢 RECOMENDACIÓN: OK PARA AVANZAR")

    st.markdown(f"**Score de alerta:** {riesgo_score} / 5")
    st.caption(f"Evaluado el: {timestamp}")

    st.divider()

    # ---------------------------
    # MODO BAYES OPCIONAL
    # ---------------------------

    st.markdown("### 🧮 Modo avanzado (opcional)")
    activar_bayes = st.checkbox("Activar análisis probabilístico (Teorema de Bayes)")

    if activar_bayes:

        st.markdown("Estimá los siguientes valores:")

        prior = st.slider(
            "Probabilidad base de que esta decisión salga mal (%)",
            0, 100, 20
        ) / 100

        evidencia = st.slider(
            "Qué tan fuerte es la señal actual de riesgo (%)",
            0, 100, riesgo_score * 20
        ) / 100

        # Bayes simplificado
        # P(Malo|Señales) ≈ prior * evidencia normalizado
        posterior = (prior * evidencia) / (
            (prior * evidencia) + ((1 - prior) * (1 - evidencia))
        )

        st.markdown("### Resultado probabilístico")

        st.write(
            f"📊 Probabilidad ajustada de que la decisión salga mal: **{round(posterior*100,2)}%**"
        )

        if posterior > 0.6:
            st.error("Alta probabilidad de error. Replantear seriamente.")
        elif posterior > 0.3:
            st.warning("Riesgo moderado. Considerar pausa.")
        else:
            st.success("Riesgo bajo según estimación probabilística.")

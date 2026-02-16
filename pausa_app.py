import streamlit as st
from datetime import datetime

# ---------------------
# Configuración
# ---------------------
st.set_page_config(page_title="💡 P.A.U.S.A. PRO", page_icon="🧠", layout="centered")

st.title("💡 P.A.U.S.A. – Decisiones bajo presión")
st.markdown("Una herramienta para frenar el impulso y pensar con claridad antes de actuar.")
st.divider()

# ---------------------
# FORMULARIO (mejor UX en celular)
# ---------------------
with st.form("form_pausa"):

    st.markdown("### Tu situación")
    idea = st.text_area("Escribí tu idea o lo que querés hacer:", "", height=100)

    impulso = st.checkbox("Esto surge por impulso")
    riesgo = st.checkbox("Podría afectar a alguien o generar problemas")
    apoyo = st.slider("¿Qué tan probable es que otros apoyen tu acción?", 0.0, 1.0, 0.5, 0.05)

    submit = st.form_submit_button("🔎 Analizar situación")

# ---------------------
# CÁLCULO SOLO SI SE ENVÍA
# ---------------------
if submit:

    # ---------------------
    # MODELO AJUSTADO (coherente)
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
    # NIVEL DE RIESGO
    # ---------------------
    if p_exito < 0.35:
        nivel = "🔴 Riesgo Alto"
        recomendacion = "Mejor no actuar ahora. Tomate tiempo."
    elif p_exito < 0.6:
        nivel = "🟡 Precaución"
        recomendacion = "Avanzá solo con un paso muy pequeño y seguro."
    else:
        nivel = "🟢 Condiciones Favorables"
        recomendacion = "Podés avanzar, pero con prudencia."

    # ---------------------
    # RESULTADOS
    # ---------------------
    st.divider()
    st.markdown("## Resultado del análisis")

    st.metric("Probabilidad estimada de resultado favorable", f"{int(p_exito*100)}%")
    st.progress(p_exito)

    st.markdown(f"### {nivel}")
    st.markdown(f"**{recomendacion}**")

    # ---------------------
    # Interpretación didáctica
    # ---------------------
    explicacion = []

    if impulso:
        explicacion.append("Detectamos que la decisión puede estar influida por impulso.")
    if riesgo:
        explicacion.append("La acción podría generar consecuencias negativas.")
    if apoyo < 0.4:
        explicacion.append("El nivel de apoyo percibido es bajo.")
    elif apoyo > 0.7:
        explicacion.append("Existe buen apoyo externo para la acción.")

    if not explicacion:
        explicacion.append("No se detectaron señales fuertes de alerta.")

    st.markdown("### Interpretación")
    for e in explicacion:
        st.write("•", e)

    # ---------------------
    # PRIMER PASO SEGURO (siempre aparece)
    # ---------------------
    st.markdown("### Definí tu próximo paso prudente")
    accion = st.text_input("¿Cuál es el paso más pequeño y seguro que podrías hacer ahora?")

    if accion:
        st.info(f"✔️ Paso definido: {accion}")

# ---------------------
# Nota legal al final
# ---------------------
st.divider()
st.warning("""
⚠️ Nota importante:  
Esta herramienta no brinda asesoramiento legal, médico, financiero ni psicológico.  
El análisis es un modelo simplificado con fines reflexivos y educativos.  
La decisión final siempre es responsabilidad del usuario.
""")

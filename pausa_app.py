import streamlit as st

st.title("🧠 Analizador de Decisiones - Safe Version")

# --- Inputs ---
idea = st.text_area("Describe tu idea o decisión:")
impulso = st.checkbox("Impulso personal")
riesgo = st.checkbox("Riesgo para otros")
apoyo = st.slider("Nivel de apoyo de terceros (0 a 1)", 0.0, 1.0, 0.5)

# --- Variables base ---
p_exito_base = 0.6
p_evidencia = 0.5 + 0.5 * apoyo  # simplificación bayesiana
p_apoyo = p_evidencia  # igual que p_evidencia para simplificar

# --- Cálculo bayesiano simplificado ---
p_exito = (p_evidencia * p_exito_base) / p_apoyo  # resultado coherente con inputs

# --- Recomendación ---
if p_exito > 0.6:
    recomendacion = "✅ Adelante"
else:
    recomendacion = "⛔ Pausa"

st.subheader("Recomendación:")
st.write(recomendacion)

# --- Historial en la sesión ---
if 'historial' not in st.session_state:
    st.session_state.historial = []

# Guardamos la decisión actual
if idea:
    st.session_state.historial.append({
        "Idea": idea,
        "Impulso": impulso,
        "Riesgo": riesgo,
        "Apoyo": apoyo,
        "Probabilidad Éxito": round(p_exito, 2),
        "Recomendación": recomendacion
    })

# Mostramos historial solo si hay más de 1 entrada
if st.session_state.historial:
    st.subheader("📜 Historial de decisiones (solo sesión activa)")
    for i, h in enumerate(st.session_state.historial[-5:], 1):  # últimas 5
        st.write(f"{i}. {h['Idea']} → {h['Recomendación']} (Éxito: {h['Probabilidad Éxito']})")

# --- Exportar decisión ---
if st.session_state.historial:
    last = st.session_state.historial[-1]
    export_text = (
        f"Idea: {last['Idea']}\n"
        f"Impulso: {last['Impulso']}\n"
        f"Riesgo: {last['Riesgo']}\n"
        f"Apoyo: {last['Apoyo']}\n"
        f"Probabilidad de Éxito: {last['Probabilidad Éxito']}\n"
        f"Recomendación: {last['Recomendación']}\n"
    )
    st.download_button("💾 Exportar decisión a TXT", data=export_text, file_name="decision.txt")

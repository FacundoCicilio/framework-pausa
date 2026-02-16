import streamlit as st
from datetime import datetime
import csv, os

# ---------------------
# CONFIG
# ---------------------
st.set_page_config(page_title="💡 P.A.U.S.A. Bayes+Juego", page_icon="🧩", layout="centered")
st.title("💡 P.A.U.S.A. Minimalista")
st.markdown("""
Tomar decisiones bajo presión puede generar errores.  
Esta versión calcula **probabilidad de éxito (Bayes)** y resultado esperado (teoría de juegos) automáticamente.
""")
st.divider()

# ---------------------
# INPUTS MÍNIMOS
# ---------------------
st.markdown("### Tu situación")
idea = st.text_area("Idea breve (opcional):", "", height=80)

impulso = st.checkbox("Siento que esto surge por impulso")
riesgo = st.checkbox("Podría afectar a alguien o generar problemas")
apoyo = st.slider("Probabilidad de que otros apoyen tu acción", 0.0, 1.0, 0.5, 0.05)

# ---------------------
# SCORE ALERTA SIMPLE
# ---------------------
score_alerta = sum([impulso, riesgo])
if apoyo > 0.7:
    score_alerta -= 0.5
elif apoyo < 0.3:
    score_alerta += 0.5

# ---------------------
# BAYES: probabilidad posterior de éxito
# ---------------------
# Probabilidad base de éxito
p_exito_base = 0.6

# Probabilidad de evidencia P(Apoyo | Éxito)
p_evidencia = 0.5 + 0.5 * apoyo  # simple lineal entre 0.5 y 1

# Probabilidad de Apoyo total P(Apoyo)
p_apoyo = 0.5 + 0.5 * apoyo  # mismo esquema, para simplificar

# Posterior: P(Éxito | Apoyo)
p_exito = (p_evidencia * p_exito_base) / p_apoyo
p_exito = min(max(p_exito, 0), 1)

# ---------------------
# TEORÍA DE JUEGOS SIMPLIFICADA
# ---------------------
# Cooperar: tu acción + apoyo de otros
cooperar = p_exito * apoyo
# No cooperar: tu acción + otros no apoyan
no_cooperar = p_exito * (1 - apoyo)

if cooperar >= no_cooperar:
    recomendacion = "🟢 Avanzar cooperando / con precaución"
else:
    recomendacion = "🔴 Pausar o replantear"

# ---------------------
# MOSTRAR RESULTADOS
# ---------------------
st.markdown("### Recomendación inmediata")
st.markdown(f"**{recomendacion}**", unsafe_allow_html=True)
st.markdown(f"Probabilidad posterior de éxito: {p_exito:.2f}")
st.markdown(f"Resultado esperado Cooperar: {cooperar:.2f} vs No Cooperar: {no_cooperar:.2f}")

# ---------------------
# PRIMER PASO CONCRETO OPCIONAL
# ---------------------
accion = ""
if recomendacion.startswith("🟢"):
    st.markdown("### Primer paso concreto")
    st.markdown("Definí una **acción pequeña y segura** para probar tu idea:")
    accion = st.text_input("Primer paso:", "")
    if accion:
        st.info(f"💡 Primer paso definido: {accion}")

# ---------------------
# REGISTRO AUTOMÁTICO EN CSV
# ---------------------
archivo_csv = "registro_ideas.csv"

def guardar():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists(archivo_csv):
        with open(archivo_csv,"w",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Fecha","Idea","Impulso","Riesgo","Apoyo","P éxito Bayes","Cooperar","No Cooperar","Recomendación","Primer paso"])
    with open(archivo_csv,"a",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, idea, impulso, riesgo, apoyo, round(p_exito,2), round(cooperar,2), round(no_cooperar,2), recomendacion, accion])

if st.button("Registrar idea y decisión"):
    guardar()
    st.success("✅ Idea registrada en el historial")

# ---------------------
# MINI TABLERO DE HISTORIAL
# ---------------------
st.divider()
st.markdown("## 🗂 Historial de ideas registradas")
if os.path.exists(archivo_csv):
    with open(archivo_csv,"r",encoding="utf-8") as f:
        st.text(f.read())
else:
    st.info("No hay ideas registradas aún.")

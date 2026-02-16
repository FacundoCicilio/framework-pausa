import streamlit as st
from datetime import datetime
import numpy as np

# -------------------------------------------------
# CONFIGURACIÓN
# -------------------------------------------------
st.set_page_config(
    page_title="💡 P.A.U.S.A. + Juego",
    page_icon="🎲",
    layout="centered"
)

# -------------------------------------------------
# ESTILO
# -------------------------------------------------
st.markdown("""
<style>
.block-container {padding-top: 2rem;}
.version-tag {color: gray; font-size: 0.9rem;}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.title("💡 P.A.U.S.A. Creativa + Teoría de Juegos")
st.markdown('<div class="version-tag">v1.1 — Captura impulso + estrategia social</div>', unsafe_allow_html=True)
st.markdown("""
Esta versión evalúa tu **impulso creativo** y también cómo tus decisiones interactúan con **otros actores**.
Tarda menos de 5 minutos.
""")
st.divider()

# -------------------------------------------------
# PASO 1: Captura rápida de idea
# -------------------------------------------------
st.markdown("## 1️⃣ Captura rápida")
st.markdown("Escribí tu idea en 3–5 líneas, sin juzgarla:")
idea = st.text_area("Tu idea:", "", height=120)

if idea:
    st.success("✅ Idea capturada con éxito!")

st.divider()

# -------------------------------------------------
# PASO 2: Filtrado tipo P.A.U.S.A.
# -------------------------------------------------
st.markdown("## 2️⃣ Filtrado rápido")
st.markdown("Marcá lo que aplique a tu idea:")

riesgo_legal = st.checkbox("Podría causar problemas legales o lastimar a alguien?")
impulso = st.checkbox("Esta idea surge solo por impulso o estado alterado?")
test_seguro = st.checkbox("Se puede probar de manera segura antes de ejecutarla?")
coherencia = st.checkbox("Es coherente con mis objetivos a mediano plazo?")

# Score de alerta
score_alerta = sum([riesgo_legal, impulso, not test_seguro, not coherencia])

st.markdown("### Score de alerta:")
st.progress(score_alerta / 4)
if score_alerta <= 1:
    st.success("🟢 Idea segura para avanzar")
elif score_alerta == 2:
    st.warning("🟡 Pausa 10 minutos antes de actuar")
else:
    st.error("🔴 Replanificar antes de ejecutar")

st.divider()

# -------------------------------------------------
# PASO 3: Mini Teoría de Juegos
# -------------------------------------------------
st.markdown("## 3️⃣ Interacción social (Teoría de Juegos)")

st.markdown("""
Marcá la **probabilidad percibida de cooperación o conflicto** de otros actores:
- 0 → Muy poco probable
- 1 → Muy probable
""")

# Sliders para 1–2 actores
actor1_coop = st.slider("Actor 1: Probabilidad de cooperar", 0.0, 1.0, 0.5, 0.05)
actor2_coop = st.slider("Actor 2 (opcional): Probabilidad de cooperar", 0.0, 1.0, 0.5, 0.05)

# Matriz de juego simple: 2x2
# Payoff: [Tu acción: Cooperar / No cooperar] vs [Actor cooperar / no cooperar]
# Valores entre 0 y 1 (riesgo vs beneficio)
payoff = np.array([
    [0.9*actor1_coop, 0.2*(1-actor1_coop)],  # Cooperar
    [0.5*actor1_coop, 0.6*(1-actor1_coop)]   # No cooperar
])

# Equilibrio simple: sumamos payoff esperado
expected_coop = payoff[0].sum()
expected_nocoop = payoff[1].sum()

st.markdown(f"**Payoff esperado Cooperar:** {expected_coop:.2f}")
st.markdown(f"**Payoff esperado No Cooperar:** {expected_nocoop:.2f}")

# Recomendación basada en equilibrio simple
if expected_coop > expected_nocoop:
    st.success("✅ Mejor opción estratégica: Cooperar / Pausar")
else:
    st.warning("⚠️ Mejor opción estratégica: No cooperar / Replanificar")

st.divider()

# -------------------------------------------------
# PASO 4: Acción mínima segura
# -------------------------------------------------
st.markdown("## 4️⃣ Transformar en proyecto seguro")
accion = st.text_area("Acción segura mínima para probar tu idea:", "", height=100)

if accion and idea:
    st.info(f"💡 Acción propuesta: {accion}")

st.divider()

# -------------------------------------------------
# PASO 5: Registro opcional
# -------------------------------------------------
st.markdown("## 5️⃣ Registro opcional")
if st.button("Registrar idea + decisión"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.success(f"Idea registrada a las {timestamp}.")
    st.code(f"Idea:\n{idea}\nScore alerta: {score_alerta}/4\nAcción segura: {accion}\nEquilibrio juego: {'Cooperar' if expected_coop>expected_nocoop else 'No cooperar'}\nFecha: {timestamp}")

st.divider()

# -------------------------------------------------
# MANIFIESTO
# -------------------------------------------------
st.markdown("## 📌 Manifiesto")
st.markdown("""
- El impulso es la chispa.  
- La estructura y el filtro racional son el combustible.  
- La interacción social puede cambiar la decisión óptima.  
- Cada idea puede transformarse en algo seguro y útil si la capturás, filtrás y evaluás estratégicamente.
""")

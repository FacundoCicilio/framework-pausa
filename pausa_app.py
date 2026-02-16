import streamlit as st
from datetime import datetime
import numpy as np

# -------------------------------------------------
# CONFIGURACIÓN
# -------------------------------------------------
st.set_page_config(
    page_title="💡 P.A.U.S.A. Creativa",
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
st.title("💡 P.A.U.S.A. Creativa + Estrategia")
st.markdown('<div class="version-tag">v1.2 — Captura impulso y evalúa interacción social</div>', unsafe_allow_html=True)
st.markdown("""
Un mini-sistema para aprovechar tu **impulso creativo** y transformarlo en ideas seguras y útiles.  
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
# PASO 2: Filtrado rápido
# -------------------------------------------------
st.markdown("## 2️⃣ Evaluación inicial")
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
# PASO 3: Evaluación de interacción social
# -------------------------------------------------
st.markdown("## 3️⃣ Considerá la interacción con otros")
st.markdown("""
Estimá cómo podrían reaccionar otros involucrados. Esto ayuda a anticipar posibles resultados antes de actuar.
""")

# Sliders para 1–2 actores
actor1_coop = st.slider("Actor 1: Probabilidad de actuar a favor de tu idea", 0.0, 1.0, 0.5, 0.05)
actor2_coop = st.slider("Actor 2 (opcional): Probabilidad de actuar a favor de tu idea", 0.0, 1.0, 0.5, 0.05)

# Matriz de resultado esperado simple
# [Tu acción: Cooperar / No cooperar] vs [Actor cooperar / no cooperar]
payoff = np.array([
    [0.9*actor1_coop, 0.2*(1-actor1_coop)],  # Cooperar
    [0.5*actor1_coop, 0.6*(1-actor1_coop)]   # No cooperar
])

expected_coop = payoff[0].sum()
expected_nocoop = payoff[1].sum()

st.markdown(f"**Resultado esperado si cooperás:** {expected_coop:.2f}")
st.markdown(f"**Resultado esperado si no cooperás:** {expected_nocoop:.2f}")

# Recomendación
if expected_coop > expected_nocoop:
    st.success("✅ Mejor opción: Cooperar / Pausar")
else:
    st.warning("⚠️ Mejor opción: No cooperar / Replanificar")

st.divider()

# -------------------------------------------------
# PASO 4: Acción mínima segura
# -------------------------------------------------
st.markdown("## 4️⃣ Definí la acción mínima segura")
accion = st.text_area("Acción mínima para probar la idea de manera segura:", "", height=100)

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
    st.code(f"""
Idea:
{idea}

Score de alerta: {score_alerta}/4

Acción mínima segura:
{accion}

Recomendación interacción social:
{'Cooperar / Pausar' if expected_coop>expected_nocoop else 'No cooperar / Replanificar'}

Fecha: {timestamp}
""")

st.divider()

# -------------------------------------------------
# MANIFIESTO
# -------------------------------------------------
st.markdown("## 📌 Manifiesto")
st.markdown("""
- El impulso es la chispa.  
- La estructura y el filtro racional son el combustible.  
- Considerar la reacción de otros mejora la decisión.  
- Cada idea puede transformarse en algo seguro y útil si la capturás, filtrás y evaluás estratégicamente.
""")

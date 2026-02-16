import streamlit as st
import requests

# ---------------------
# Configuración
# ---------------------
st.set_page_config(page_title="💡 P.A.U.S.A. PRO", page_icon="🧠", layout="centered")

# Estado persistente
if "analisis_realizado" not in st.session_state:
    st.session_state.analisis_realizado = False

if "resultado" not in st.session_state:
    st.session_state.resultado = {}

# ---------------------
# TÍTULO
# ---------------------
st.title("💡 P.A.U.S.A. – Decisiones bajo presión")
st.markdown(
    "Modelo reflexivo basado en probabilidad y análisis estratégico para frenar el impulso y decidir con claridad."
)
st.divider()

# ---------------------
# FUNCIÓN DIDÁCTICA
# ---------------------
def generar_interpretacion(idea, p_exito, nivel, impulso, riesgo, apoyo):

    contexto = f"""
Situación:
{idea}

Probabilidad estimada: {int(p_exito*100)}%
Nivel: {nivel}
Impulso: {impulso}
Riesgo: {riesgo}
Apoyo: {apoyo}

Redactá una interpretación clara, estratégica y reflexiva.
No menciones modelos matemáticos ni inteligencia artificial.
Explicá qué actitud conviene adoptar.
"""

    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    payload = {"inputs": contexto}

    try:
        response = requests.post(API_URL, json=payload, timeout=15)
        data = response.json()

        if isinstance(data, list) and "generated_text" in data[0]:
            texto = data[0]["generated_text"]
            return texto.replace(contexto, "").strip()
        else:
            return "El resultado sugiere actuar con prudencia y evaluar estratégicamente el siguiente movimiento."

    except:
        return "El resultado sugiere actuar con prudencia y evaluar estratégicamente el siguiente movimiento."


# ---------------------
# FORMULARIO PRINCIPAL
# ---------------------
with st.form("form_pausa"):

    st.markdown("### Tu situación")
    idea = st.text_area("Escribí tu idea o lo que querés hacer:", "", height=100)

    impulso = st.checkbox("Esto surge por impulso")
    riesgo = st.checkbox("Podría afectar a alguien o generar problemas")

    apoyo = st.slider(
        "¿Qué tan probable es que otros apoyen tu acción?",
        0.0, 1.0, 0.5, 0.05
    )

    submit = st.form_submit_button("🔎 Evaluar decisión")

# ---------------------
# CÁLCULO DEL MODELO
# ---------------------
if submit:

    p_exito_base = 0.6

    penalizacion = 0
    if impulso:
        penalizacion += 0.2
    if riesgo:
        penalizacion += 0.3

    bonus_apoyo = 0.25 * apoyo

    p_exito = p_exito_base - penalizacion + bonus_apoyo
    p_exito = min(max(p_exito, 0.1), 0.9)

    if p_exito < 0.35:
        nivel = "Riesgo Alto"
        recomendacion = "Conviene no actuar ahora. Replanteá la estrategia."
    elif p_exito < 0.6:
        nivel = "Precaución"
        recomendacion = "Avanzá solo con un paso pequeño y reversible."
    else:
        nivel = "Condiciones Favorables"
        recomendacion = "Podés avanzar, manteniendo prudencia."

    # Guardar resultados
    st.session_state.resultado = {
        "idea": idea,
        "p_exito": p_exito,
        "nivel": nivel,
        "recomendacion": recomendacion,
        "impulso": impulso,
        "riesgo": riesgo,
        "apoyo": apoyo
    }

    st.session_state.analisis_realizado = True

# ---------------------
# MOSTRAR RESULTADOS (persistentes)
# ---------------------
if st.session_state.analisis_realizado:

    r = st.session_state.resultado

    st.divider()
    st.markdown("## Resultado del análisis estratégico")

    st.metric(
        "Probabilidad estimada de resultado favorable",
        f"{int(r['p_exito']*100)}%"
    )

    st.progress(r["p_exito"])

    st.markdown(f"### {r['nivel']}")
    st.markdown(f"**{r['recomendacion']}**")

    # Interpretación básica estructural
    st.markdown("### Factores detectados")

    if r["impulso"]:
        st.write("• La decisión presenta señales de impulso.")
    if r["riesgo"]:
        st.write("• Existen posibles consecuencias negativas para terceros.")
    if r["apoyo"] < 0.4:
        st.write("• El apoyo externo es bajo, lo que reduce estabilidad estratégica.")
    elif r["apoyo"] > 0.7:
        st.write("• El apoyo externo es sólido, lo que mejora la posición estratégica.")

    if not r["impulso"] and not r["riesgo"]:
        st.write("• No se detectan señales críticas inmediatas.")

    # Interpretación ampliada
    st.markdown("### Interpretación reflexiva")

    with st.spinner("Generando análisis reflexivo..."):
        interpretacion = generar_interpretacion(
            r["idea"],
            r["p_exito"],
            r["nivel"],
            r["impulso"],
            r["riesgo"],
            r["apoyo"]
        )

    st.markdown(interpretacion)

    # ---------------------
    # PASO ESTRATÉGICO
    # ---------------------
    st.markdown("### Definí tu próximo paso prudente")

    accion = st.text_input(
        "¿Cuál es el paso más pequeño y seguro que podrías hacer ahora?"
    )

    if st.button("Confirmar paso estratégico"):
        if accion.strip() != "":
            st.success(f"✔ Paso definido: {accion}")
            st.info(
                "Sugerencia: realizalo pronto para evitar que el impulso vuelva a dominar la decisión."
            )

# ---------------------
# NOTA FINAL
# ---------------------
st.divider()
st.warning("""
Esta herramienta es un modelo simplificado con fines reflexivos y educativos.
No constituye asesoramiento legal, médico, financiero ni psicológico.
La decisión final siempre es responsabilidad del usuario.
""")

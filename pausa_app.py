import streamlit as st
import requests

# ---------------------
# Configuración
# ---------------------
st.set_page_config(page_title="💡 P.A.U.S.A. PRO", page_icon="🧠", layout="centered")

# ---------------------
# Estado persistente
# ---------------------
if "analisis_realizado" not in st.session_state:
    st.session_state.analisis_realizado = False

if "resultado" not in st.session_state:
    st.session_state.resultado = {}

# ---------------------
# Filtro básico de contenido peligroso
# ---------------------
def contenido_peligroso(texto):
    palabras_riesgo = [
        "matar", "arma", "disparar", "cuchillo",
        "golpear", "atacar", "explosivo",
        "envenenar", "suicidar", "violencia"
    ]
    texto = texto.lower()
    return any(p in texto for p in palabras_riesgo)

# ---------------------
# Evaluación estratégica del paso
# ---------------------
def evaluar_paso(accion, nivel):

    accion_lower = accion.lower()

    aumenta_opciones = any(p in accion_lower for p in [
        "buscar", "explorar", "averiguar",
        "analizar", "investigar", "hablar",
        "preguntar", "actualizar cv"
    ])

    irreversible = any(p in accion_lower for p in [
        "renunciar", "denunciar", "terminar",
        "cortar relación", "demandar"
    ])

    confrontativo = any(p in accion_lower for p in [
        "enfrentar", "reclamar", "exigir"
    ])

    if irreversible:
        return "⚠ Paso de alto impacto: puede ser difícil de revertir. Evaluá consecuencias antes de ejecutarlo."

    if aumenta_opciones:
        if nivel == "Precaución":
            return "✔ Estrategia coherente: aumenta tus opciones sin cerrar caminos. Es consistente con un escenario de incertidumbre."
        elif nivel == "Condiciones Favorables":
            return "✔ Buen movimiento estratégico: fortalece tu posición manteniendo flexibilidad."
        else:
            return "✔ Paso prudente: preserva opcionalidad en un contexto de riesgo."

    if confrontativo and nivel == "Riesgo Alto":
        return "⚠ Movimiento confrontativo en contexto riesgoso. Puede escalar el conflicto."

    return "Movimiento neutral. Evaluá cómo impacta tu poder de negociación y tus alternativas futuras."

# ---------------------
# Interpretación didáctica
# ---------------------
def generar_interpretacion(idea, p_exito, nivel):

    if nivel == "Riesgo Alto":
        return "El escenario presenta baja probabilidad de resultado favorable. Conviene pausar y evitar decisiones irreversibles."

    if nivel == "Precaución":
        return "Existe incertidumbre relevante. Las decisiones que preserven opciones y reduzcan exposición son estratégicamente más sólidas."

    return "Las condiciones son relativamente favorables. Aun así, mantener prudencia mejora la estabilidad del resultado."


# ---------------------
# Título
# ---------------------
st.title("💡 P.A.U.S.A. – Decisiones bajo presión")
st.markdown(
    "Modelo reflexivo basado en probabilidad y análisis estratégico para ayudarte a frenar el impulso y decidir con claridad."
)
st.divider()

# ---------------------
# Formulario principal
# ---------------------
with st.form("form_pausa"):

    st.markdown("### Tu situación")
    idea = st.text_area("Escribí tu idea o lo que querés hacer:", "", height=150)

    impulso = st.checkbox("Esto surge por impulso")
    riesgo = st.checkbox("Podría afectar a alguien o generar problemas")

    apoyo = st.slider(
        "¿Qué tan probable es que otros apoyen tu acción?",
        0.0, 1.0, 0.5, 0.05
    )

    submit = st.form_submit_button("🔎 Evaluar decisión")

# ---------------------
# Bloqueo preventivo
# ---------------------
if submit and contenido_peligroso(idea):
    st.error("La acción planteada implica daño o ilegalidad.")
    st.warning("La herramienta no puede analizar este tipo de situaciones.")
    st.stop()

# ---------------------
# Cálculo del modelo
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
        recomendacion = "Conviene no actuar ahora."
    elif p_exito < 0.6:
        nivel = "Precaución"
        recomendacion = "Avanzá solo con un paso pequeño y reversible."
    else:
        nivel = "Condiciones Favorables"
        recomendacion = "Podés avanzar con prudencia."

    st.session_state.resultado = {
        "idea": idea,
        "p_exito": p_exito,
        "nivel": nivel,
        "recomendacion": recomendacion
    }

    st.session_state.analisis_realizado = True

# ---------------------
# Mostrar resultados
# ---------------------
if st.session_state.analisis_realizado:

    r = st.session_state.resultado

    st.divider()
    st.markdown("## Resultado del análisis estratégico")

    st.metric("Probabilidad estimada de resultado favorable", f"{int(r['p_exito']*100)}%")
    st.progress(r["p_exito"])

    st.markdown(f"### {r['nivel']}")
    st.markdown(f"**{r['recomendacion']}**")

    st.markdown("### Interpretación")
    st.write(generar_interpretacion(r["idea"], r["p_exito"], r["nivel"]))

    # ---------------------
    # Paso estratégico
    # ---------------------
    st.markdown("### Definí tu próximo paso prudente")

    accion = st.text_input("¿Cuál es el paso más pequeño y seguro que podrías hacer ahora?")

    if st.button("Confirmar paso estratégico"):

        if accion.strip() == "":
            st.warning("Definí un paso antes de confirmar.")

        elif contenido_peligroso(accion):
            st.error("El paso propuesto implica daño o ilegalidad.")
            st.stop()

        else:
            st.success(f"✔ Paso definido: {accion}")

            evaluacion = evaluar_paso(accion, r["nivel"])
            st.info(evaluacion)

# ---------------------
# Nota final
# ---------------------
st.divider()
st.warning("""
Esta herramienta es un modelo simplificado con fines reflexivos y educativos.
No constituye asesoramiento legal, médico, financiero ni psicológico.
La decisión final siempre es responsabilidad del usuario.
""")

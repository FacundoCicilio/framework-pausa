import streamlit as st
import re

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

if "accion_confirmada" not in st.session_state:
    st.session_state.accion_confirmada = False


# ---------------------
# Normalización de texto
# ---------------------
def normalizar(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto


# ---------------------
# Filtros adaptados a Argentina
# ---------------------
def contenido_violento(texto):
    palabras = [
        "matar", "arma", "disparar", "cuchillo",
        "golpear", "atacar", "explosivo",
        "envenenar", "violencia",
        "cagar a trompadas", "romper todo",
        "hacer mierda", "apuñalar"
    ]
    texto = normalizar(texto)
    return any(re.search(rf"\b{re.escape(p)}\b", texto) for p in palabras)


def contenido_ilegal(texto):
    palabras = [
        "droga", "traficar", "estafa", "fraude",
        "robar", "hackear", "lavar dinero",
        "evadir impuestos", "afip",
        "denuncia falsa", "coima",
        "soborno", "meter preso sin pruebas",
        "cagar a alguien", "hacer una estafa",
        "negro sin facturar"
    ]
    texto = normalizar(texto)
    return any(re.search(rf"\b{re.escape(p)}\b", texto) for p in palabras)


def alto_impacto_terceros(texto):
    palabras = [
        "embarazada", "hijo", "hija",
        "niño", "niña", "bebé",
        "abandonar", "divorcio con hijos",
        "tenencia", "cuota alimentaria",
        "echar a alguien", "despedir",
        "dejar sin trabajo"
    ]
    texto = normalizar(texto)
    return any(re.search(rf"\b{re.escape(p)}\b", texto) for p in palabras)


# ---------------------
# Clasificación de riesgo
# ---------------------
def clasificar_riesgo(texto):

    if contenido_violento(texto):
        return "bloqueado"

    if contenido_ilegal(texto):
        return "riesgo_extremo"

    if alto_impacto_terceros(texto):
        return "impacto_terceros"

    return "normal"


# ---------------------
# Evaluación estratégica del paso
# ---------------------
def evaluar_paso(accion):

    accion_lower = normalizar(accion)

    aumenta_opciones = any(p in accion_lower for p in [
        "buscar", "explorar", "averiguar",
        "analizar", "investigar", "hablar",
        "preguntar", "actualizar cv",
        "postular"
    ])

    irreversible = any(p in accion_lower for p in [
        "renunciar", "denunciar", "terminar",
        "cortar relacion", "demandar"
    ])

    if irreversible:
        return "⚠ Paso de alto impacto: puede ser difícil de revertir."

    if aumenta_opciones:
        return "✔ Paso prudente: aumenta tus opciones sin cerrar caminos."

    return "Movimiento neutral. Evaluá cómo impacta tu poder de negociación."


# ---------------------
# Interpretación general
# ---------------------
def generar_interpretacion(nivel):

    if nivel == "Riesgo Alto":
        return "Escenario desfavorable. Evitá decisiones irreversibles."

    if nivel == "Precaución":
        return "Existe incertidumbre. Las decisiones reversibles son más sólidas."

    return "Condiciones relativamente favorables, pero mantené prudencia."


# ---------------------
# UI
# ---------------------
st.title("💡 P.A.U.S.A. – Decisiones bajo presión")
st.markdown(
    "Modelo reflexivo basado en probabilidad y análisis estratégico para ayudarte a frenar el impulso y decidir con claridad."
)
st.divider()

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
# Lógica principal
# ---------------------
if submit:

    clasificacion = clasificar_riesgo(idea)

    if clasificacion == "bloqueado":
        st.error("La acción implica violencia. No se puede procesar.")
        st.stop()

    p_base = 0.6
    penalizacion = 0

    if impulso:
        penalizacion += 0.2

    if riesgo:
        penalizacion += 0.25

    if clasificacion == "riesgo_extremo":
        penalizacion += 0.35

    if clasificacion == "impacto_terceros":
        penalizacion += 0.15

    bonus_apoyo = 0.25 * apoyo

    p_exito = p_base - penalizacion + bonus_apoyo
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
        "p_exito": p_exito,
        "nivel": nivel,
        "recomendacion": recomendacion
    }

    st.session_state.analisis_realizado = True
    st.session_state.accion_confirmada = False


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
    st.write(generar_interpretacion(r["nivel"]))

    st.divider()
    st.markdown("### Definí tu próximo paso prudente")

    accion = st.text_input("¿Cuál es el paso más pequeño y seguro que podrías hacer ahora?")

    if st.button("Confirmar paso estratégico"):

        if accion.strip() == "":
            st.warning("Definí un paso antes de confirmar.")

        elif clasificar_riesgo(accion) == "bloqueado":
            st.error("El paso implica violencia.")

        else:
            st.session_state.accion_confirmada = True
            st.session_state.accion_texto = accion

    if st.session_state.accion_confirmada:
        st.success(f"✔ Paso definido: {st.session_state.accion_texto}")
        evaluacion = evaluar_paso(st.session_state.accion_texto)
        st.info(evaluacion)


st.divider()
st.warning("""
Esta herramienta es un modelo simplificado con fines reflexivos y educativos.
No constituye asesoramiento legal, médico, financiero ni psicológico.
La decisión final siempre es responsabilidad del usuario.
""")

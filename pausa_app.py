import streamlit as st

st.set_page_config(page_title="P.A.U.S.A. – Decisiones bajo presión")

st.title("💡 P.A.U.S.A. – Decisiones bajo presión")
st.write("Modelo reflexivo basado en probabilidad y análisis estratégico para ayudarte a frenar el impulso y decidir con claridad.")

# =============================
# FUNCIONES DE FILTRO
# =============================

def contenido_violento(texto):
    palabras = [
        "matar", "arma", "disparar", "cuchillo",
        "golpear", "atacar", "explosivo",
        "envenenar", "violencia"
    ]
    texto = texto.lower()
    return any(p in texto for p in palabras)


def contenido_ilegal(texto):
    palabras = [
        "droga", "vender droga", "traficar",
        "estafa", "fraude", "robar",
        "hackear", "lavar dinero",
        "contrabando"
    ]
    texto = texto.lower()
    return any(p in texto for p in palabras)


def alto_impacto_terceros(texto):
    palabras = [
        "embarazada",
        "hijo",
        "niño",
        "abandonar",
        "dejar a mi hijo",
        "divorcio con hijos",
        "echar a alguien",
        "despedir",
        "romper familia"
    ]
    texto = texto.lower()
    return any(p in texto for p in palabras)

# =============================
# MODELO PROBABILÍSTICO
# =============================

def calcular_probabilidad(prob_apoyo, impacto_negativo, riesgo_irreversibilidad, alto_impacto):

    prior = 0.6  # optimismo estratégico base

    ajuste = (
        prob_apoyo * 0.4
        - impacto_negativo * 0.3
        - riesgo_irreversibilidad * 0.2
    )

    if alto_impacto:
        ajuste -= 0.15  # penalización por terceros vulnerables

    posterior = prior + ajuste

    return max(0.01, min(0.99, posterior))

# =============================
# INTERFAZ
# =============================

st.subheader("Tu situación")
idea = st.text_area("Escribí tu idea o lo que querés hacer:")

st.subheader("¿Qué tan probable es que otros apoyen tu acción?")
prob_apoyo = st.slider("", 0.0, 1.0, 0.5)

submit = st.button("Analizar")

# =============================
# BLOQUEO DE CONTENIDO GRAVE
# =============================

if submit and idea:

    if contenido_violento(idea):
        st.error("La acción planteada implica violencia. No puede analizarse.")
        st.stop()

    if contenido_ilegal(idea):
        st.error("La acción planteada implica ilegalidad. No puede analizarse.")
        st.warning("La herramienta no optimiza ni evalúa actividades ilegales.")
        st.stop()

    # =============================
    # ANÁLISIS ESTRATÉGICO
    # =============================

    impacto_negativo = 0.5
    riesgo_irreversibilidad = 0.4
    impacto_alto = alto_impacto_terceros(idea)

    posterior = calcular_probabilidad(
        prob_apoyo,
        impacto_negativo,
        riesgo_irreversibilidad,
        impacto_alto
    )

    st.subheader("Resultado del análisis estratégico")
    st.metric("Probabilidad estimada de resultado favorable", f"{int(posterior*100)}%")

    # Precaución según probabilidad
    if posterior < 0.4:
        st.error("Alto riesgo estratégico. Reevaluá antes de actuar.")
    elif posterior < 0.6:
        st.warning("Precaución: avanzá solo con un paso pequeño y reversible.")
    else:
        st.success("Movimiento estratégicamente razonable si se ejecuta con prudencia.")

    if impacto_alto:
        st.warning(
            "La decisión involucra terceros en situación vulnerable. "
            "Se recomienda extrema prudencia y explorar alternativas que reduzcan daño colateral."
        )

    st.write("Interpretación reflexiva")
    st.write(
        "El resultado sugiere frenar la acción impulsiva y evaluar consecuencias, "
        "poder de negociación futuro y reversibilidad."
    )

    # =============================
    # DEFINICIÓN DEL PASO PRUDENTE
    # =============================

    st.subheader("Definí tu próximo paso prudente")
    accion = st.text_input("¿Cuál es el paso más pequeño y seguro que podrías hacer ahora?")

    if accion:

        if contenido_violento(accion) or contenido_ilegal(accion):
            st.error("El paso propuesto implica violencia o ilegalidad. No puede validarse.")
            st.stop()

        st.success(f"✔ Paso definido: {accion}")

        if "renunciar" in accion.lower():
            st.warning("Movimiento irreversible. Evaluá alternativas antes de ejecutarlo.")
        elif "hablar" in accion.lower() or "consultar" in accion.lower():
            st.success("Paso prudente: aumenta información y mantiene opciones abiertas.")
        else:
            st.info("Movimiento neutral. Evaluá cómo impacta tus alternativas futuras.")

# =============================
# DISCLAIMER
# =============================

st.markdown("---")
st.caption(
    "Esta herramienta es un modelo simplificado con fines reflexivos y educativos. "
    "No constituye asesoramiento legal, médico, financiero ni psicológico. "
    "La decisión final siempre es responsabilidad del usuario."
)

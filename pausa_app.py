import streamlit as st
from datetime import datetime
import smtplib
from email.message import EmailMessage

# ---------------------
# Configuración de la app
# ---------------------
st.set_page_config(page_title="💡 P.A.U.S.A. Amigable", page_icon="🧩", layout="centered")
st.title("💡 P.A.U.S.A. – Decisiones bajo presión")

st.markdown("Tomar decisiones bajo presión puede generar errores. Esta herramienta te ayuda a **frenar el impulso y pensar de manera segura**.")
st.divider()

# ---------------------
# Inputs mínimos
# ---------------------
st.markdown("### Tu situación")
idea = st.text_area("Escribí tu idea o lo que querés hacer (opcional):", "", height=80)

impulso = st.checkbox("Esto surge por impulso")
riesgo = st.checkbox("Podría afectar a alguien o generar problemas")
apoyo = st.slider("¿Qué tan probable es que otros apoyen tu acción?", 0.0, 1.0, 0.5, 0.05)

# ---------------------
# Score de alerta interno
# ---------------------
score_alerta = sum([impulso, riesgo])
if apoyo > 0.7:
    score_alerta -= 0.5
elif apoyo < 0.3:
    score_alerta += 0.5

# ---------------------
# BAYES SIMPLIFICADO (interno)
# ---------------------
p_exito_base = 0.6
p_evidencia = 0.5 + 0.5 * apoyo
p_apoyo = 0.5 + 0.5 * apoyo
p_exito = (p_evidencia * p_exito_base) / p_apoyo
p_exito = min(max(p_exito, 0), 1)

# ---------------------
# TEORÍA DE JUEGOS SIMPLIFICADA (interno)
# ---------------------
cooperar = p_exito * apoyo
no_cooperar = p_exito * (1 - apoyo)

if cooperar >= no_cooperar:
    recomendacion = "🟢 Podés avanzar con precaución"
else:
    recomendacion = "⚠️ Mejor pausar o replantear tu acción"

# ---------------------
# Interpretación amigable
# ---------------------
def interpretacion_amigable(p_exito, cooperar, no_cooperar, recomendacion):
    if p_exito < 0.4:
        exito_texto = "Bajas chances de que salga bien"
    elif p_exito < 0.7:
        exito_texto = "Medias chances de que salga bien"
    else:
        exito_texto = "Altas chances de que salga bien"

    if cooperar > no_cooperar:
        coop_texto = "Si otros apoyan, esto tiene más chances de funcionar"
    else:
        coop_texto = "Si otros no apoyan, cuidado, podría salir mal"

    return f"{exito_texto}. {coop_texto}. Recomendación: {recomendacion}."

mensaje_amigable = interpretacion_amigable(p_exito, cooperar, no_cooperar, recomendacion)

# ---------------------
# Mostrar resultados
# ---------------------
st.markdown("### Recomendación inmediata")
st.markdown(f"**{mensaje_amigable}**")

# ---------------------
# Primer paso seguro
# ---------------------
accion = ""
if recomendacion.startswith("🟢"):
    st.markdown("### Primer paso seguro")
    st.markdown("Definí **una acción pequeña y segura** que podés hacer primero:")
    accion = st.text_input("Qué harías primero:", "")
    if accion:
        st.info(f"💡 Primer paso definido: {accion}")

# ---------------------
# Enviar idea por mail (opcional)
# ---------------------
st.divider()
st.markdown("### Enviar tu idea por email (opcional)")
email_destino = st.text_input("Ingresá tu email para recibir la idea:")
if st.button("Enviar idea por email") and email_destino:
    try:
        msg = EmailMessage()
        msg.set_content(f"Idea: {idea}\nImpulso: {impulso}\nRiesgo: {riesgo}\nApoyo: {apoyo}\nInterpretación: {mensaje_amigable}\nPrimer paso: {accion}")
        msg["Subject"] = "Registro de tu idea - Framework P.A.U.S.A."
        msg["From"] = "TU_EMAIL@gmail.com"   # <-- reemplazar con tu email
        msg["To"] = email_destino

        # Usar SMTP (ejemplo Gmail)
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("TU_EMAIL@gmail.com", "TU_CONTRASEÑA")  # <-- reemplazar
        server.send_message(msg)
        server.quit()
        st.success("✅ Idea enviada por email correctamente")
    except Exception as e:
        st.error(f"❌ No se pudo enviar el email: {e}")

# ---------------------
# Nota final
# ---------------------
st.warning("""
⚠️ Nota importante:  
Esta herramienta **no da consejos personales, legales, médicos ni de seguridad vial**.  
Solo ofrece un **análisis de tu situación usando probabilidades y teoría de juegos** para ayudarte a pensar antes de actuar.  
Los resultados reflejan un **escenario hipotético y simplificado**; tu juicio personal siempre es lo más importante.
""")

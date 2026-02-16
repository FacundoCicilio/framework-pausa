if registrar:
    if st.button("Enviar ahora"):
        try:
            msg = EmailMessage()
            contenido = f"""
Nueva idea registrada en Framework P.A.U.S.A.

Idea/Comentario: {idea}
Impulso: {impulso}
Riesgo: {riesgo}
Apoyo: {apoyo}
Interpretación: {mensaje_amigable}
Primer paso: {accion}
Fecha/Hora: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
            # Forzar codificación UTF-8
            msg.set_content(contenido, charset='utf-8')

            msg["Subject"] = "Nueva idea registrada - Framework P.A.U.S.A."
            msg["From"] = "TU_EMAIL@gmail.com"  # <-- reemplazar con tu email
            msg["To"] = "cuentasnacionalesgrana@gmail.com"

            # SMTP seguro (Gmail ejemplo)
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("TU_EMAIL@gmail.com", "TU_CONTRASEÑA")  # <-- reemplazar con app password
            server.send_message(msg)
            server.quit()
            st.success("✅ Tu idea fue enviada correctamente")
        except Exception as e:
            st.error(f"❌ No se pudo enviar el email: {e}")

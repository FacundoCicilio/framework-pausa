from datetime import datetime

def framework_pausa(idea="", impulso=False, riesgo=False, apoyo=0.5, accion=""):
    """
    Framework P.A.U.S.A. - Decisiones bajo presión
    
    Parámetros:
    - idea: str, idea o comentario del usuario (opcional)
    - impulso: bool, si la acción surge por impulso
    - riesgo: bool, si puede afectar a alguien o generar problemas
    - apoyo: float (0 a 1), probabilidad de que otros apoyen la acción
    - accion: str, primer paso seguro definido por el usuario (opcional)
    
    Retorna:
    - dict con interpretación amigable, recomendación y primer paso
    """
    
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

    interpretacion = f"{exito_texto}. {coop_texto}. Recomendación: {recomendacion}."

    # ---------------------
    # Resultado final
    # ---------------------
    resultado = {
        "interpretacion": interpretacion,
        "recomendacion": recomendacion,
        "primer_paso": accion,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return resultado


# ---------------------
# Ejemplo de uso
# ---------------------
if __name__ == "__main__":
    # Probando la función
    ejemplo = framework_pausa(
        idea="Quiero tomar un vino pero tengo que manejar",
        impulso=True,
        riesgo=True,
        apoyo=0.5,
        accion="Definir acción pequeña y segura"
    )
    print(ejemplo)

def explicacion_automatica(resultado, meta=1000):

    if resultado.empty:
        return (
            "✅ Todas las tiendas cumplen la meta semanal.\n\n"
            "No se detectan riesgos operativos en el período analizado."
        )

    total = len(resultado)

    promedio = resultado["Promedio en Órdenes"].mean()
    min_orders = resultado["Promedio en Órdenes"].min()
    max_orders = resultado["Promedio en Órdenes"].max()

    peor = resultado.loc[
        resultado["Promedio en Órdenes"].idxmin()
    ]

    severidad = abs(peor["Diferencia_vs_Meta"])

    if severidad > 500:
        nivel = "CRÍTICO"
    elif severidad > 250:
        nivel = "ALTO"
    else:
        nivel = "MODERADO"

    texto = f"""
🧠 ANÁLISIS AUTOMÁTICO (IA LOCAL)

• Tiendas analizadas: {total}
• Promedio de órdenes del grupo: {promedio:.0f}
• Rango de desempeño: {min_orders:.0f} – {max_orders:.0f}

🚨 TIENDA MÁS CRÍTICA
• Tienda: {peor['Store']}
• Órdenes: {peor['Promedio en Órdenes']}
• Diferencia vs meta: {peor['Diferencia_vs_Meta']}
• Nivel de severidad: {nivel}

📉 INTERPRETACIÓN
El incumplimiento no es un evento puntual. Existe un grupo de tiendas
con desempeño consistentemente bajo que está afectando el promedio
general. La meta de {meta} órdenes no es homogénea para todas las tiendas.

🎯 RECOMENDACIONES
• Evaluar metas diferenciadas por tipo de tienda
• Analizar causas locales (demanda, ubicación, operación)
• Separar tiendas low-volume del promedio global
"""
    return texto

import pandas as pd

def analisis_tiendas(
    df,
    anio=None,
    semana=None,
    meta=1000,
    estado="todos"  # "cumplen", "no_cumplen", "todos"
):
    df_filtro = df.copy()

    if anio is not None:
        df_filtro = df_filtro[df_filtro["AnioContable"] == anio]

    if semana is not None:
        if isinstance(semana, list):
            df_filtro = df_filtro[df_filtro["SemanaContable"].isin(semana)]
        else:
            df_filtro = df_filtro[df_filtro["SemanaContable"] == semana]

    resumen = (
        df_filtro
        .groupby(["AnioContable", "SemanaContable", "Store"], as_index=False)
        ["Promedio en Órdenes"]
        .sum()
    )

    resumen["Diferencia_vs_Meta"] = resumen["Promedio en Órdenes"] - meta
    resumen["Estado"] = resumen["Promedio en Órdenes"].apply(
        lambda x: "Cumple" if x >= meta else "No cumple"
    )

    if estado == "cumplen":
        resumen = resumen[resumen["Estado"] == "Cumple"]
    elif estado == "no_cumplen":
        resumen = resumen[resumen["Estado"] == "No cumple"]

    return resumen.sort_values(
        ["AnioContable", "SemanaContable", "Promedio en Órdenes"]
    )

import matplotlib.pyplot as plt

def grafico_tiendas(resultado, meta=1000):

    if resultado.empty:
        return None

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(
        resultado["Store"],
        resultado["Promedio en Órdenes"]
    )

    ax.axhline(
        y=meta,
        linestyle="--",
        color="red",
        label="Meta semanal (1000)"
    )

    ax.set_title("Tiendas vs Meta Semanal")
    ax.set_ylabel("Órdenes")
    ax.set_xlabel("Tienda")
    ax.legend()
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    return fig

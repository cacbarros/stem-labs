from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def generate_linearization_plot(out_pdf=None, show=True, seed=0):
    """
    Linearizacao Ec vs v^2 (2-em-1):
      - show=True  -> mostra no Jupyter/Colab
      - guarda sempre PDF

    out_pdf:
      - None: guarda por defeito em ../assets/linearizacao_plot.pdf
              (calculado a partir da localizacao deste ficheiro)
      - str/Path: caminho explicitamente fornecido
    """

    # --- Resolver caminho de saida de forma robusta ---
    here = Path(__file__).resolve().parent          # .../src_graphics
    base = here.parent                               # .../energia_movimentos
    if out_pdf is None:
        out_pdf = base / "assets" / "linearizacao_plot.pdf"
    else:
        out_pdf = Path(out_pdf)

    out_pdf.parent.mkdir(parents=True, exist_ok=True)

    # --- Dados simulados (v^2 em m^2/s^2, Ec em J) ---
    v2 = np.array([0, 1, 4, 9, 16, 25], dtype=float)
    m_real = 0.5  # kg

    rng = np.random.default_rng(seed)
    ec = 0.5 * m_real * v2 + rng.normal(0.0, 0.1, size=len(v2))  # ruido pequeno

    # --- Ajuste linear Ec = a*v^2 + b ---
    a, b = np.polyfit(v2, ec, 1)

    fig, ax = plt.subplots(figsize=(6ी(6, 3.5))
    ax.scatter(v2, ec, label="Dados experimentais")
    ax.plot(v2, a * v2 + b, label=fr"Ajuste: $E_c = {a:.3f}v^2 + {b:.3f}$")

    ax.set_xlabel(r"$v^2\ (\mathrm{m^2\,s^{-2}})$")
    ax.set_ylabel(r"$E_c\ (\mathrm{J})$")
    ax.set_title("Linearizacao: Determinacao da massa", fontsize=10)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.7)

    fig.tight_layout()
    fig.savefig(out_pdf, format="pdf", bbox_inches="tight")

    if show:
        plt.show()

    plt.close(fig)
    return out_pdf, a, b


if __name__ == "__main__":
    path, a, b = generate_linearization_plot(show=False)
    print(f"Saved: {path} | a={a:.6f} | b={b:.6f}")


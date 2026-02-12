from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def generate_linearization_plot(
    out_pdf="../assets/linearizacao_plot.pdf",
    show=True,
    seed=0,
):
    """
    Linearizacao Ec vs v^2 (2-em-1):
      - show=True  -> mostra no Jupyter/interactive
      - guarda sempre PDF (out_pdf)

    Colocar este ficheiro em:
      physics10/energia_movimentos/src_graphics/linearizacao_massa.py

    Saida (por defeito) em:
      physics10/energia_movimentos/assets/linearizacao_plot.pdf
    """

    # --- Dados simulados (v^2 em m^2/s^2, Ec em J) ---
    v2 = np.array([0, 1, 4, 9, 16, 25], dtype=float)
    m_real = 0.5  # kg

    rng = np.random.default_rng(seed)
    ec = 0.5 * m_real * v2 + rng.normal(0.0, 0.1, size=len(v2))  # ruido pequeno

    # --- Ajuste linear Ec = a*v^2 + b ---
    a, b = np.polyfit(v2, ec, 1)

    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.scatter(v2, ec, label="Dados experimentais")
    ax.plot(v2, a * v2 + b, label=fr"Ajuste: $E_c = {a:.3f}v^2 + {b:.3f}$")

    ax.set_xlabel(r"$v^2\ (\mathrm{m^2\,s^{-2}})$")
    ax.set_ylabel(r"$E_c\ (\mathrm{J})$")
    ax.set_title("Linearizacao: Determinacao da massa", fontsize=10)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.7)

    fig.tight_layout()

    out_path = Path(out_pdf)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, format="pdf", bbox_inches="tight")

    if show:
        plt.show()

    plt.close(fig)
    return out_path, a, b


if __name__ == "__main__":
    path, a, b = generate_linearization_plot(show=False)
    print(f"Saved: {path} | a={a:.6f} | b={b:.6f}")


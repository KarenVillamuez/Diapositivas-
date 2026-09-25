#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Figuras del articulo LHXT 2026, version 2.
Rotulos en ingles para que sobrevivan a la traduccion sin rehacer nada.
Paleta validada con el verificador de la guia de visualizacion:
  blue #2a78d6 / orange #eb6834, todas las comprobaciones en PASS.
"""
import csv, json, os, statistics as st
from pathlib import Path
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

PAPER_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = Path(__file__).resolve().parents[4]
OUT = os.environ.get("FIGOUT", str(PAPER_ROOT / "figuras"))
BENCH = os.environ.get("BENCH", str(PROJECT_ROOT / "logs" / "benchmarks"))
os.makedirs(OUT, exist_ok=True)

# ---------- sistema visual ----------
S1, S2 = "#2a78d6", "#eb6834"          # categorico, validado
S1L, S2L = "#a9c9ee", "#f7c0a8"        # versiones claras para bandas secundarias
INK, MUT, FAINT = "#0b0b0b", "#52514e", "#d7d6d2"
SURF = "#ffffff"

# --------------------------------------------------------------------------
# TIPOGRAFIA. Cambiar estas dos constantes cambia toda la tipografia de las
# seis figuras. Alternativas instaladas y probadas:
#   "Latin Modern Roman"          serif de LaTeX, la que se usa por defecto
#   "Latin Modern Roman Demi"     la misma, mas gruesa, para titulos
#   "Latin Modern Roman Dunhill"  ascendentes muy altas, decorativa
#   "Latin Modern Sans"           version sans de la misma familia
#   "Liberation Serif"            metricamente igual a Times New Roman
#   "Carlito"                     metricamente igual a Calibri
# Para inclinar los rotulos anadir FONT_STYLE = "italic" mas abajo.
FONT      = "Times New Roman"
FONT_HEAD = "Times New Roman"
# --------------------------------------------------------------------------

plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF,
    "font.family": FONT, "font.size": 13.2,
    "text.color": INK, "axes.labelcolor": MUT,
    "xtick.color": MUT, "ytick.color": MUT,
    "axes.edgecolor": FAINT, "axes.linewidth": 0.9,
    "xtick.major.size": 0, "ytick.major.size": 0,
    "legend.frameon": False,
    "mathtext.fontset": "cm", "mathtext.default": "it",
})

def clean(ax, grid="y"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    if grid:
        ax.grid(True, axis=grid, color=FAINT, linewidth=0.8)
        ax.set_axisbelow(True)

def title(ax, head, sub=None):
    ax.set_title(head, fontsize=14.5, family=FONT_HEAD, color=INK, loc="left", pad=14 if sub else 10)
    if sub:
        ax.text(0, 1.035, sub, transform=ax.transAxes, fontsize=11.6, color=MUT,
                ha="left", va="bottom")

# ---------- datos ----------
def load(model_dir, fname):
    with open(os.path.join(BENCH, model_dir, fname), encoding="utf-8") as fh:
        d = json.load(fh)
    rows = d["results"] if isinstance(d, dict) else d
    return {r["question_id"]: r for r in rows if r["config_id"] == "cfg_eval_full"}

P, Q = "Phi-4-mini-instruct-Q4_K_M", "Qwen2.5-3B-Instruct-Q4_K_M"
SEEDS = ["42", "7", "123", "2026"]
RUNS = {
    "Phi-4-mini":  dict(zip(SEEDS, ["benchmark_20260902_140238.json", "benchmark_20260903_122324.json",
                                    "benchmark_20260903_125347.json", "benchmark_20260903_131956.json"])),
    "Qwen2.5-3B": dict(zip(SEEDS, ["benchmark_20260902_144618.json", "benchmark_20260903_123651.json",
                                   "benchmark_20260903_130631.json", "benchmark_20260903_135021.json"])),
}
DIRS = {"Phi-4-mini": P, "Qwen2.5-3B": Q}
D = {m: {s: load(DIRS[m], f) for s, f in r.items()} for m, r in RUNS.items()}
MODELS = ["Phi-4-mini", "Qwen2.5-3B"]
CONT = ["G1", "G2", "G3", "G4", "V1", "V2", "V3", "W1", "W2", "W3", "R1", "R2"]
W_G, W_R, W_L = 0.40, 0.40, 0.20

def lvl(r):
    v = (r["overall_score"] - W_G * r["grounding_score"] - W_R * r["relevance_score"]) / W_L
    return max(0.0, min(1.0, v))

# Valoraciones docentes: una sola fuente trazable para texto y figuras.
RATERS = {"Rater 1": {}, "Rater 2": {}}
with open(PAPER_ROOT / "anclaje-docente" / "captura_docentes.csv", encoding="utf-8-sig", newline="") as fh:
    for row in csv.DictReader(fh):
        key = "Rater 1" if row["evaluador"] == "docente_1" else "Rater 2"
        RATERS[key][row["codigo"]] = tuple(int(row[k]) for k in ("correccion", "claridad", "adecuacion_nivel"))
AUTO = {"R01":0.839,"R02":0.844,"R03":0.856,"R04":0.653,"R05":0.806,"R06":0.826,
        "R07":0.766,"R08":0.859,"R09":0.814,"R10":0.842}
CODES = sorted(AUTO)

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=300, bbox_inches="tight", facecolor=SURF)
    plt.close(fig)
    print("  ", name)


# ===================================================================== FIG 1
# Anatomia del puntaje: una sola barra, tres franjas, explicadas en palabras.
def fig1():
    fig, ax = plt.subplots(figsize=(9.0, 2.85))
    segs = [(0.40, S1,  "grounding"), (0.40, S1L, "relevance"), (0.20, "#e8c977", "level")]
    x = 0.0
    for w, c, lab in segs:
        ax.add_patch(FancyBboxPatch((x + 0.004, 0.35), w - 0.008, 0.30,
                     boxstyle="round,pad=0,rounding_size=0.012",
                     facecolor=c, edgecolor=SURF, linewidth=2))
        ax.text(x + w / 2, 0.50, f"{int(w*100)} %", ha="center", va="center",
                fontsize=17.4, family=FONT_HEAD, color="#ffffff" if c == S1 else INK)
        x += w
    notes = [
        (0.20, "grounding\ncompares the ANSWER\nwith the retrieved text", INK),
        (0.60, "relevance\ncompares the QUESTION\nwith the retrieved text", INK),
        (0.90, "level\nuses ANSWER LENGTH", INK),
    ]
    for cx, txt, col in notes:
        ax.text(cx, 0.27, txt, ha="center", va="top", fontsize=11.1, color=col, linespacing=1.45)
    ax.annotate("the answer is not an input here",
                xy=(0.60, 0.655), xytext=(0.60, 0.80),
                ha="center", fontsize=11.8, color=S2, family=FONT_HEAD,
                arrowprops=dict(arrowstyle="-|>", color=S2, linewidth=1.8,
                                shrinkA=2, shrinkB=4))
    ax.set_xlim(-0.01, 1.01); ax.set_ylim(-0.16, 1.26)
    ax.axis("off")
    ax.text(0, 1.20, "Anatomy of the number the tutor reports as “quality”",
            fontsize=15.1, family=FONT_HEAD, color=INK, va="top")
    ax.text(0, 1.05, "60 % depends on the output: 40 % on meaning and 20 % on length.",
            fontsize=12.2, color=MUT, va="top")
    save(fig, "F1_score_anatomy.png")


# ===================================================================== FIG 2
# Descomposicion por pregunta: la franja intermedia es identica entre modelos.
def fig2():
    from matplotlib.patches import Patch
    LVL = "#e8c977"
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.1), sharey=True)
    for ax, m in zip(axes, MODELS):
        g = [W_G * D[m]["42"][q]["grounding_score"] for q in CONT]
        r = [W_R * D[m]["42"][q]["relevance_score"] for q in CONT]
        l = [W_L * lvl(D[m]["42"][q]) for q in CONT]
        x = np.arange(len(CONT))
        ax.bar(x, g, 0.68, color=S1, linewidth=2, edgecolor=SURF)
        ax.bar(x, r, 0.68, bottom=g, color=S1L, linewidth=2, edgecolor=SURF)
        ax.bar(x, l, 0.68, bottom=np.add(g, r), color=LVL, linewidth=2, edgecolor=SURF)
        ax.set_xticks(x); ax.set_xticklabels(CONT, fontsize=10.4)
        ax.set_ylim(0, 1.0)
        ax.text(0.5, 1.03, m, transform=ax.transAxes, ha="center", fontsize=13.3,
                family=FONT_HEAD, color=INK)
        clean(ax)
    axes[0].set_ylabel("Reported score")
    fig.tight_layout(rect=[0, 0, 1, 0.80])
    fig.text(0.007, 0.985, "What the score is made of, question by question",
             fontsize=15.1, family=FONT_HEAD, color=INK, va="top", ha="left")
    fig.text(0.007, 0.925, "Grounding uses answer meaning; level uses answer length. "
                           "Relevance does not inspect the answer directly.",
             fontsize=12.1, color=MUT, va="top", ha="left")
    fig.legend(handles=[Patch(facecolor=S1, label="grounding  (answer vs retrieved text)"),
                        Patch(facecolor=S1L, label="relevance  (question vs retrieved text)"),
                        Patch(facecolor=LVL, label="level  (word count)")],
               loc="upper left", bbox_to_anchor=(0.005, 0.885), ncol=3,
               frameon=False, fontsize=11.0, handlelength=1.2, handleheight=1.0,
               handletextpad=0.5, columnspacing=1.6)
    save(fig, "F2_score_by_question.png")


# ===================================================================== FIG 3
# Ruido frente a senal: lo que cambia al repetir vs lo que cambia al cambiar de modelo.
def fig3():
    sd, dif = [], []
    for q in CONT:
        sds = [st.stdev([D[m][s][q]["overall_score"] for s in SEEDS]) for m in MODELS]
        mus = [st.mean(D[m][s][q]["overall_score"] for s in SEEDS) for m in MODELS]
        sd.append(st.mean(sds)); dif.append(abs(mus[0] - mus[1]))
    noise, signal = st.mean(sd), st.mean(dif)

    fig = plt.figure(figsize=(9.4, 3.9))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 2.15], wspace=0.28)

    ax0 = fig.add_subplot(gs[0])
    ax0.barh([1, 0], [noise, signal], 0.5, color=[S2, S1], linewidth=2, edgecolor=SURF)
    for y, v, lab in ((1, noise, "mean within-model SD\nper question"),
                      (0, signal, "mean absolute difference\nbetween model means")):
        ax0.text(v + 0.0015, y, f"{v:.3f}", va="center", fontsize=13.9, family=FONT_HEAD, color=INK)
        ax0.text(0, y - 0.37, lab, va="top", fontsize=10.8, color=MUT, linespacing=1.4)
    ax0.set_xlim(0, max(noise, signal) * 1.35); ax0.set_ylim(-0.85, 1.6)
    ax0.set_yticks([]); ax0.set_xticks([])
    for s in ("top", "right", "left", "bottom"):
        ax0.spines[s].set_visible(False)
    ax0.text(0, 1.34, "Two descriptive summaries", transform=ax0.transAxes,
             fontsize=12.8, family=FONT_HEAD, color=INK, va="bottom")
    ax0.text(0, 1.27, "Different definitions; shown\ntogether for scale, not as a\nformal signal-to-noise ratio.",
             transform=ax0.transAxes, fontsize=10.9, color=MUT, linespacing=1.4, va="top")

    ax1 = fig.add_subplot(gs[1])
    x = np.arange(len(CONT))
    for i, (m, c) in enumerate(zip(MODELS, (S1, S2))):
        mu = [st.mean(D[m][s][q]["overall_score"] for s in SEEDS) for q in CONT]
        e = [st.stdev([D[m][s][q]["overall_score"] for s in SEEDS]) for q in CONT]
        ax1.errorbar(x + (i - 0.5) * 0.22, mu, yerr=e, fmt="o", color=c, capsize=0,
                     markersize=6.5, elinewidth=2.6, markeredgecolor=SURF, markeredgewidth=1.5,
                     linestyle="none", label=m)
    ax1.set_xticks(x); ax1.set_xticklabels(CONT, fontsize=10.4)
    ax1.set_ylim(0.60, 0.96); ax1.set_ylabel("Reported score")
    ax1.legend(loc="lower left", fontsize=11.0, ncol=2, handletextpad=0.4, columnspacing=1.2,
               frameon=True, facecolor=SURF, edgecolor="none", framealpha=0.9)
    clean(ax1)
    ax1.text(0, 1.055, "Each dot is an average of four seeds; the bar is its spread",
             transform=ax1.transAxes, fontsize=12.1, color=MUT)
    ax1.text(0, 1.17, "Observed means and standard deviations by question",
             transform=ax1.transAxes, fontsize=14.5, family=FONT_HEAD, color=INK)
    save(fig, "F3_noise_vs_signal.png")


# ===================================================================== FIG 4
# Slopegraph: los dos docentes sobre las mismas diez respuestas.
def fig4():
    fig, ax = plt.subplots(figsize=(7.8, 4.7))
    m1 = {c: st.mean(RATERS["Rater 1"][c]) for c in CODES}
    m2 = {c: st.mean(RATERS["Rater 2"][c]) for c in CODES}
    for c in CODES:
        up = m2[c] >= m1[c]
        col = S1 if up else S2
        ax.plot([0, 1], [m1[c], m2[c]], color=col, linewidth=2.1, alpha=0.85,
                solid_capstyle="round", zorder=2)
        ax.scatter([0, 1], [m1[c], m2[c]], s=46, color=col, zorder=3,
                   edgecolor=SURF, linewidth=1.6)
    # una etiqueta por nivel, agrupando los codigos que comparten valor
    for side, mm, ha, dx in ((0, m1, "right", -0.04), (1, m2, "left", 0.04)):
        byval = {}
        for c in CODES:
            byval.setdefault(round(mm[c], 3), []).append(c)
        for v, cs in byval.items():
            cs = sorted(cs)
            lines = [", ".join(cs[i:i + 3]) for i in range(0, len(cs), 3)]
            ax.text(side + dx, v, "\n".join(lines), ha=ha, va="center",
                    fontsize=10.7, color=MUT, linespacing=1.35)

    ax.set_xlim(-0.42, 1.30); ax.set_ylim(0.7, 5.2)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["Rater 1", "Rater 2"], fontsize=13.3, family=FONT_HEAD)
    ax.set_ylabel("Mean rating  (1 to 5)")
    ax.set_yticks([1, 2, 3, 4, 5])
    clean(ax, grid="y")
    ax.spines["bottom"].set_visible(False)
    ax.text(0, 1.20, "The same ten answers, judged by two English teachers",
            transform=ax.transAxes, fontsize=14.8, family=FONT_HEAD, color=INK)
    ax.text(0, 1.055, "Each line is one answer. This ten-answer pilot did not establish adequate agreement\n"
                     "(Spearman $\\rho$ = −0.50; Cohen’s $\\kappa$ = −0.43 for use without modification).",
            transform=ax.transAxes, fontsize=11.8, color=MUT, linespacing=1.5)
    save(fig, "F4_two_raters_slopegraph.png")


# ===================================================================== FIG 5
# Puntaje automatico frente al juicio humano.
def fig5():
    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    for (name, col, mk) in (("Rater 1", S1, "o"), ("Rater 2", S2, "s")):
        xs = [AUTO[c] for c in CODES]
        ys = [st.mean(RATERS[name][c]) for c in CODES]
        ax.scatter(xs, ys, s=78, color=col, marker=mk, label=name, zorder=3,
                   edgecolor=SURF, linewidth=1.7, alpha=0.92)
        rho, p = stats.spearmanr(xs, ys)
        ax.plot([min(xs), max(xs)], [st.mean(ys)] * 2, color=col, linewidth=1.6,
                linestyle=(0, (4, 3)), alpha=0.65, zorder=2)
        ax.text(max(xs), st.mean(ys) + 0.10, f"{name}: $\\rho$ = {rho:+.2f}",
                ha="right", va="bottom", fontsize=11.4, color=col, family=FONT_HEAD)
    ax.set_xlabel("Score reported by the system")
    ax.set_ylabel("Teacher rating  (1 to 5)")
    ax.set_xlim(0.635, 0.878); ax.set_ylim(0.6, 5.2)
    ax.set_yticks([1, 2, 3, 4, 5])
    clean(ax)
    ax.legend(loc="upper left", fontsize=11.4, ncol=2)
    ax.text(0, 1.17, "No monotonic association is evident in this ten-answer pilot",
            transform=ax.transAxes, fontsize=14.8, family=FONT_HEAD, color=INK)
    ax.text(0, 1.055, "Dashed lines mark each teacher’s mean; coefficients are exploratory.",
            transform=ax.transAxes, fontsize=11.8, color=MUT)
    save(fig, "F5_auto_vs_human.png")


# ===================================================================== FIG 6
# Transformacion afin de cada componente semantico.
def fig6():
    fig, ax = plt.subplots(figsize=(7.6, 3.3))
    raw = np.linspace(-1, 1, 200)
    ax.plot(raw, (raw + 1) / 2, color=S1, linewidth=2.6, zorder=3)
    ax.plot([-1, 1], [0, 1], color=FAINT, linewidth=0)  # marco
    pts = [(0.00, 0.50), (0.20, 0.60)]
    for rx, ry in pts:
        ax.plot([-1, rx], [ry, ry], color=S2, linewidth=1.4, linestyle=(0, (3, 3)), zorder=2)
        ax.plot([rx, rx], [0, ry], color=S2, linewidth=1.4, linestyle=(0, (3, 3)), zorder=2)
        ax.scatter([rx], [ry], s=64, color=S2, zorder=4, edgecolor=SURF, linewidth=1.6)
    ax.annotate("0.00 raw = 0.50 mapped",
                xy=(0.00, 0.50), xytext=(-0.55, 0.34),
                fontsize=11.1, color=INK, family=FONT_HEAD,
                arrowprops=dict(arrowstyle="-|>", color=S2, linewidth=1.4))
    ax.annotate("0.20 raw = 0.60 mapped",
                xy=(0.20, 0.60), xytext=(0.34, 0.52),
                fontsize=11.1, color=INK, family=FONT_HEAD,
                arrowprops=dict(arrowstyle="-|>", color=S2, linewidth=1.4))
    ax.set_xlim(-1.02, 1.02); ax.set_ylim(0, 1.02)
    ax.set_xlabel("Raw cosine similarity")
    ax.set_ylabel("Mapped component score")
    clean(ax, grid=None)
    ax.grid(True, color=FAINT, linewidth=0.8); ax.set_axisbelow(True)
    ax.text(0, 1.20, "Affine mapping applied to each semantic component",
            transform=ax.transAxes, fontsize=14.8, family=FONT_HEAD, color=INK)
    ax.text(0, 1.055, "It preserves rank. It does not convert the composite 0.60 threshold into one raw cosine.",
            transform=ax.transAxes, fontsize=11.8, color=MUT)
    save(fig, "F6_scale_compression.png")


if __name__ == "__main__":
    print("Figuras escritas en", OUT)
    fig1(); fig2(); fig3(); fig4(); fig5(); fig6()

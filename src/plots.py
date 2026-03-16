import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns

# Global 20% font size increase for axes, ticks, and legends
plt.rcParams.update({
    'axes.labelsize': 14.4,    # default 12 * 1.2
    'axes.titlesize': 15.6,    # default 13 * 1.2
    'xtick.labelsize': 12,     # default 10 * 1.2
    'ytick.labelsize': 12,     # default 10 * 1.2
    'legend.fontsize': 10.8,   # default 9 * 1.2
    'legend.title_fontsize': 12,
})

_cmap = plt.colormaps["cubehelix"]

MODEL_STYLES = [
    ("m1", _cmap(0.25), "M1: Unadjusted"),
    ("m2", _cmap(0.5),  "M2: + Sex"),
    ("m3", _cmap(0.75), "M3: + Sex + Age"),
]


def run_pathology_regression(pathology_name, pathology_type, surv_df, path_all_df, dose_vals):
    """Run 3 logistic regression models for a given pathology."""
    affected = path_all_df[path_all_df["Pathology"] == pathology_name]["Animal Number"].unique()

    df_r = surv_df[["Animal Number", "Sex", "Dose", "Days on Study"]].copy()
    df_r["has_pathology"] = df_r["Animal Number"].isin(affected).astype(int)
    df_r["Sex_M"] = (df_r["Sex"] == "Male").astype(int)

    n_affected = df_r["has_pathology"].sum()
    if n_affected < 5 or n_affected > len(df_r) - 5:
        return None

    results = {}

    for dose in dose_vals:
        grp = df_r[df_r["Dose"] == dose]
        results[f"prev_{dose}"] = 100 * grp["has_pathology"].mean() if len(grp) > 0 else 0

    try:
        models = [
            ("m1", ["Dose"]),
            ("m2", ["Dose", "Sex_M"]),
            ("m3", ["Dose", "Sex_M", "Days on Study"]),
        ]
        for prefix, cols in models:
            X = sm.add_constant(df_r[cols])
            m = sm.Logit(df_r["has_pathology"], X).fit(disp=0)
            ci = m.conf_int().loc["Dose"]
            results[f"{prefix}_dose_coef"] = m.params["Dose"]
            results[f"{prefix}_dose_or"] = np.exp(m.params["Dose"])
            results[f"{prefix}_dose_or_lo"] = np.exp(ci[0])
            results[f"{prefix}_dose_or_hi"] = np.exp(ci[1])
            results[f"{prefix}_dose_p"] = m.pvalues["Dose"]
            if prefix == "m3":
                results["m3_days_p"] = m.pvalues["Days on Study"]
                results["m3_days_or"] = np.exp(m.params["Days on Study"])
    except Exception:
        return None

    results["pathology"] = pathology_name
    results["type"] = pathology_type
    results["n_affected"] = n_affected
    results["n_total"] = len(df_r)
    results["prev_pct"] = 100 * n_affected / len(df_r)
    return results


def format_results(results_df, pathology_type):
    """Format results table for display."""
    subset = results_df[results_df["type"] == pathology_type].sort_values("m1_dose_p").copy()
    display_df = pd.DataFrame({
        "Pathology": subset["pathology"],
        "N": subset["n_affected"].astype(int),
        "Prev%": subset["prev_pct"].round(1),
        "M1: OR": subset["m1_dose_or"].round(3),
        "M1: p": subset["m1_dose_p"].round(4),
        "M2: OR": subset["m2_dose_or"].round(3),
        "M2: p": subset["m2_dose_p"].round(4),
        "M3: OR": subset["m3_dose_or"].round(3),
        "M3: p": subset["m3_dose_p"].round(4),
        "M3: Days OR": subset["m3_days_or"].round(4),
        "M3: Days p": subset["m3_days_p"].round(4),
    }).reset_index(drop=True)
    return display_df


def plot_forest(results_df, pathology_type, title, significant_only=False):
    """Forest plot of dose odds ratios per pathology across three models."""
    subset = results_df[results_df["type"] == pathology_type].sort_values("m3_dose_or", ascending=True).copy()
    if significant_only:
        subset = subset[subset["m3_dose_p"] < 0.05]
    if len(subset) == 0:
        print(f"No {pathology_type} pathologies to plot.")
        return

    n_paths = len(subset)
    fig_height = max(5, n_paths * 0.55 + 2)
    fig, ax = plt.subplots(figsize=(10, fig_height))

    offsets = [-0.2, 0, 0.2]

    for (prefix, color, label), offset in zip(MODEL_STYLES, offsets):
        or_col = f"{prefix}_dose_or"
        lo_col = f"{prefix}_dose_or_lo"
        hi_col = f"{prefix}_dose_or_hi"

        y_pos = np.arange(n_paths) + offset
        ors = subset[or_col].values
        lo = subset[lo_col].values
        hi = subset[hi_col].values

        xerr = np.array([ors - lo, hi - ors])
        ax.errorbar(ors, y_pos, xerr=xerr, fmt="o", color=color,
                    markersize=5, capsize=3, linewidth=1.2, label=label, zorder=3)

    for j, (_, row) in enumerate(subset.iterrows()):
        p = row["m3_dose_p"]
        if p < 0.001: star = "***"
        elif p < 0.01: star = "**"
        elif p < 0.05: star = "*"
        else: continue
        x_max = max(row[f"{pfx}_dose_or_hi"] for pfx in ["m1", "m2", "m3"])
        ax.text(x_max * 1.02 if ax.get_xscale() == "log" else x_max + 0.002,
                j - 0.1, star, va="center", ha="left", fontsize=14.4, fontweight="bold", color="#d62728")

    ax.axvline(1.0, color="black", linestyle="--", linewidth=1, alpha=0.7, zorder=1)
    ax.set_yticks(np.arange(n_paths))
    ax.set_yticklabels([f"{row['pathology']}  (n={row['n_affected']})"
                        for _, row in subset.iterrows()], fontsize=10.8)
    ax.set_xlabel("Odds Ratio per 1 W/kg increase in radiation dose")
    ax.set_title(f"{title}\n(* = adjusted dose trend p<0.05)", fontsize=15.6)
    ax.legend(loc="lower right", fontsize=10.8)
    ax.grid(axis="x", alpha=0.3)

    all_hi = subset["m1_dose_or_hi"].max()
    all_lo = subset["m1_dose_or_lo"].min()
    if all_hi / max(all_lo, 0.01) > 5:
        ax.set_xscale("log")
        ax.set_xlabel("Odds Ratio per 1 W/kg (95% CI, log scale)")

    ax.text(0.02, -0.08, "← Less disease with radiation", transform=ax.transAxes, ha="left", va="top", fontsize=10.8, color="gray")
    ax.text(0.98, -0.08, "More disease with radiation →", transform=ax.transAxes, ha="right", va="top", fontsize=10.8, color="gray")

    plt.tight_layout(rect=[0, 0.02, 1, 0.96])
    sns.despine()
    plt.show()


def plot_prevalence_bars(results_df, pathology_type, title, dose_vals, dose_colors, dose_bar_labels):
    """Horizontal bar chart of pathology prevalence by dose group."""
    subset = results_df[results_df["type"] == pathology_type].sort_values("n_affected", ascending=True).copy()
    if len(subset) == 0:
        print(f"No {pathology_type} pathologies to plot.")
        return

    n_paths = len(subset)
    fig_height = max(5, n_paths * 0.5 + 1.5)
    fig, ax = plt.subplots(figsize=(12, fig_height))

    bar_width = 0.2
    y_positions = np.arange(n_paths)

    for i, (dose, color, label) in enumerate(zip(dose_vals, dose_colors, dose_bar_labels)):
        col = f"prev_{dose}"
        offsets = y_positions + (i - 1.5) * bar_width
        ax.barh(offsets, subset[col], height=bar_width, color=color,
                label=label, edgecolor="white", linewidth=0.5)

    for j, (_, row) in enumerate(subset.iterrows()):
        max_prev = max(row[f"prev_{d}"] for d in dose_vals)
        star = ""
        if row["m3_dose_p"] < 0.001: star = "***"
        elif row["m3_dose_p"] < 0.01: star = "**"
        elif row["m3_dose_p"] < 0.05: star = "*"
        if star:
            ax.text(max_prev + 0.5, j, star, va="center", ha="left",
                    fontsize=13.2, fontweight="bold", color="#d62728")

    ax.set_yticks(y_positions)
    ax.set_yticklabels(subset["pathology"], fontsize=10.8)
    ax.set_xlabel("Prevalence (%)")
    ax.set_title(f"{title}\n(* = dose trend p<0.05, adjusted for sex + age)", fontsize=15.6)
    ax.legend(title="Dose (SAR)", loc="lower right", fontsize=10.8)
    ax.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    sns.despine()
    plt.show()

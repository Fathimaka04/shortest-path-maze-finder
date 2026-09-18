"""
UI Components Module for Wayfinder
Gaming HUD Theme: Animated Cyberpunk Grid & Neon Controls
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from visualization.plotter import ALGO_COLORS


def inject_custom_css():
    """Injects animated synthwave grid background and cyberpunk HUD styling."""
    st.markdown(
        """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Share+Tech+Mono&display=swap');

        /* Dynamic Animated Grid Canvas Background */
        .stApp {
            background-color: #030308;
            background-image: 
                linear-gradient(rgba(0, 240, 255, 0.08) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 240, 255, 0.08) 1px, transparent 1px);
            background-size: 32px 32px;
            background-position: -1px -1px;
            animation: gridMove 25s linear infinite;
        }

        @keyframes gridMove {
            0% { background-position: 0 0; }
            100% { background-position: 32px 32px; }
        }

        /* Gamer HUD Card Containers */
        div[data-testid="stColumn"] {
            background: linear-gradient(135deg, rgba(13, 14, 25, 0.95) 0%, rgba(5, 6, 12, 0.98) 100%);
            border-radius: 12px;
            border: 1px solid #00F0FF;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.2), inset 0 0 15px rgba(0, 240, 255, 0.05);
            padding: 24px;
        }

        /* Neon Subheadings */
        h3 {
            font-family: 'Orbitron', sans-serif !important;
            letter-spacing: 2px;
            color: #00F0FF !important;
            text-shadow: 0 0 8px rgba(0, 240, 255, 0.6);
            padding-top: 0rem;
            text-transform: uppercase;
        }

        /* --- BUTTON CUSTOMIZATIONS --- */
        /* Secondary Action Button: Maze Generation (Neon Cyan / Electric Blue) */
        div[data-testid="stButton"] > button:not([kind="primary"]) {
            font-family: 'Orbitron', sans-serif;
            border-radius: 6px;
            font-weight: 700;
            background: linear-gradient(90deg, #00C8FF 0%, #0072FF 100%);
            color: #FFFFFF !important;
            border: none;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            box-shadow: 0 0 12px rgba(0, 200, 255, 0.4);
            transition: all 0.2s ease-in-out;
        }
        div[data-testid="stButton"] > button:not([kind="primary"]):hover {
            background: linear-gradient(90deg, #00E5FF 0%, #0099FF 100%);
            box-shadow: 0 0 22px rgba(0, 229, 255, 0.8);
            transform: translateY(-2px);
        }

        /* Primary Action Button: Run Comparison (Electric Magenta / Cyber Pink) */
        div[data-testid="stButton"] > button[kind="primary"] {
            font-family: 'Orbitron', sans-serif;
            border-radius: 6px;
            font-weight: 700;
            background: linear-gradient(90deg, #FF0055 0%, #FF2A75 100%);
            color: #FFFFFF !important;
            border: none;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            box-shadow: 0 0 15px rgba(255, 0, 85, 0.5);
            transition: all 0.2s ease-in-out;
        }
        div[data-testid="stButton"] > button[kind="primary"]:hover {
            background: linear-gradient(90deg, #FF2A75 0%, #FF5599 100%);
            box-shadow: 0 0 25px rgba(255, 0, 85, 0.9);
            transform: translateY(-2px);
        }

        /* Gamer Metric KPI Cards */
        div[data-testid="stMetricValue"] {
            font-family: 'Share Tech Mono', monospace;
            color: #39FF14 !important;
            text-shadow: 0 0 10px rgba(57, 255, 20, 0.5);
        }

        /* Sleek Data Frame Borders */
        div[data-testid="stDataFrame"] {
            border: 1px solid #39FF14;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(57, 255, 20, 0.15);
        }
    </style>
    """,
        unsafe_allow_html=True,
    )


def render_gaming_title():
    """Renders a custom arcade-style title banner."""
    st.markdown(
        """
        <div style="text-align: center; padding: 10px 0px 20px 0px;">
            <h1 style="font-family: 'Orbitron', sans-serif; font-size: 48px; font-weight: 900; 
                       background: linear-gradient(90deg, #00F0FF, #FF0055); -webkit-background-clip: text; 
                       -webkit-text-fill-color: transparent; text-shadow: 0 0 20px rgba(0, 240, 255, 0.4); 
                       margin: 0; letter-spacing: 3px;">
                  WAYFINDER 
            </h1>
            <p style="font-family: 'Share Tech Mono', monospace; color: #39FF14; font-size: 16px; 
                      letter-spacing: 2px; margin-top: 5px; text-transform: uppercase; text-shadow: 0 0 8px rgba(57, 255, 20, 0.6);">
                [ INTERACTIVE PATHFINDING & MAZE BENCHMARK HUB ]
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_legend(benchmark_data):
    """Renders HUD-style color-coded algorithm badges."""
    legend_cols = st.columns(len(benchmark_data))
    for idx, res in enumerate(benchmark_data):
        algo = res["algorithm"]
        color = ALGO_COLORS.get(algo, "#FF2A6D")
        legend_cols[idx].markdown(
            f"""
            <div style="background: rgba(0,0,0,0.6); border: 1px solid {color}; border-radius: 6px; padding: 6px 10px; text-align: center; box-shadow: 0 0 8px {color}66;">
                <span style="color:{color}; font-family: 'Orbitron', sans-serif; font-weight: bold; font-size: 13px;">▶ {algo}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_benchmarks(benchmark_data):
    """Renders high-score metrics, benchmark tables, and dark arcade performance charts."""
    fastest = min(benchmark_data, key=lambda x: x["execution_time_ms"])
    most_efficient = min(benchmark_data, key=lambda x: x["nodes_explored"])

    # High Score KPI Highlights
    col_m1, col_m2 = st.columns(2)
    col_m1.metric(
        "⚡ SPEED KING",
        fastest["algorithm"],
        f"{fastest['execution_time_ms']:.2f} ms",
    )
    col_m2.metric(
        "🎯 MAX EFFICIENCY",
        most_efficient["algorithm"],
        f"{most_efficient['nodes_explored']} cells",
    )

    st.divider()

    # Empirical Results Table
    df = pd.DataFrame(benchmark_data)
    table_df = df[
        ["algorithm", "path_length", "nodes_explored", "execution_time_ms"]
    ].copy()
    table_df.columns = ["Algorithm", "Path Cost", "Nodes Explored", "Time (ms)"]
    st.dataframe(table_df, use_container_width=True, hide_index=True)

    # Dark Arcade Performance Bar Charts
    st.write("**PERFORMANCE METRICS:**")
    fig_graph, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(4, 5.5), facecolor="#0D0E15"
    )

    algos = df["algorithm"]
    bar_colors = [ALGO_COLORS.get(a, "#00F0FF") for a in algos]

    # Chart 1: Search Space
    ax1.set_facecolor("#050508")
    ax1.barh(algos, df["nodes_explored"], color=bar_colors, edgecolor="#FFFFFF", linewidth=0.8)
    ax1.set_title(
        "NODES EXPLORED (LOWER = BETTER)",
        color="#00F0FF",
        fontsize=9,
        fontweight="bold",
        pad=6,
    )
    ax1.tick_params(colors="#FFFFFF", labelsize=8)
    ax1.spines["bottom"].set_color("#00F0FF")
    ax1.spines["left"].set_color("#00F0FF")
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # Chart 2: Execution Time (ms)
    ax2.set_facecolor("#050508")
    ax2.barh(algos, df["execution_time_ms"], color=bar_colors, edgecolor="#FFFFFF", linewidth=0.8)
    ax2.set_title(
        "EXECUTION TIME (MS)",
        color="#00F0FF",
        fontsize=9,
        fontweight="bold",
        pad=6,
    )
    ax2.tick_params(colors="#FFFFFF", labelsize=8)
    ax2.spines["bottom"].set_color("#00F0FF")
    ax2.spines["left"].set_color("#00F0FF")
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    plt.tight_layout()
    st.pyplot(fig_graph, use_container_width=True)

    st.caption(
        f"🎮 **TOP PERFORMER:** `{most_efficient['algorithm']}` evaluated the fewest nodes ({most_efficient['nodes_explored']} cells)."
    )
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from visualization.plotter import ALGO_COLORS

def inject_custom_css():
    """Injects dark-theme card and button styling."""
    st.markdown("""
    <style>
        div[data-testid="stColumn"] {
            background-color: #1A1D24;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #2E3440;
        }
        .stButton>button {
            border-radius: 8px;
            font-weight: 600;
        }
        h3 {
            padding-top: 0rem;
        }
    </style>
    """, unsafe_allow_html=True)

def render_legend(benchmark_data):
    """Renders color-coded legend for active algorithms."""
    legend_cols = st.columns(len(benchmark_data))
    for idx, res in enumerate(benchmark_data):
        algo = res["algorithm"]
        color = ALGO_COLORS.get(algo, "#FF2A6D")
        legend_cols[idx].markdown(
            f"<span style='color:{color}; font-weight:bold; font-size:15px;'>━━ {algo}</span>", 
            unsafe_allow_html=True
        )

def render_benchmarks(benchmark_data):
    """Renders KPI metrics, benchmark table, and Matplotlib bar charts."""
    fastest = min(benchmark_data, key=lambda x: x["execution_time_ms"])
    most_efficient = min(benchmark_data, key=lambda x: x["nodes_explored"])

    col_m1, col_m2 = st.columns(2)
    col_m1.metric("Fastest Run", fastest["algorithm"], f"{fastest['execution_time_ms']:.2f} ms")
    col_m2.metric("Fewest Nodes", most_efficient["algorithm"], f"{most_efficient['nodes_explored']} cells")

    st.divider()

    # Data Table
    df = pd.DataFrame(benchmark_data)
    table_df = df[["algorithm", "path_length", "nodes_explored", "execution_time_ms"]].copy()
    table_df.columns = ["Algorithm", "Path Cost", "Nodes Explored", "Time (ms)"]
    st.dataframe(table_df, use_container_width=True, hide_index=True)

    # Performance Charts
    st.write("**Performance Charts:**")
    fig_graph, (ax1, ax2) = plt.subplots(2, 1, figsize=(4, 5.5), facecolor="#FFFFFF")
    
    algos = df["algorithm"]
    bar_colors = [ALGO_COLORS.get(a, "#4A90E2") for a in algos]

    # Graph 1: Search Space
    ax1.set_facecolor("#FFFFFF")
    ax1.barh(algos, df["nodes_explored"], color=bar_colors)
    ax1.set_title("Nodes Explored (Lower = Better)", color="#000000", fontsize=10, fontweight="bold", pad=5)
    ax1.tick_params(colors="#000000", labelsize=9)
    ax1.spines["bottom"].set_color("#000000")
    ax1.spines["left"].set_color("#000000")
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # Graph 2: Execution Time
    ax2.set_facecolor("#FFFFFF")
    ax2.barh(algos, df["execution_time_ms"], color=bar_colors)
    ax2.set_title("Execution Time in ms (Lower = Better)", color="#000000", fontsize=10, fontweight="bold", pad=5)
    ax2.tick_params(colors="#000000", labelsize=9)
    ax2.spines["bottom"].set_color("#000000")
    ax2.spines["left"].set_color("#000000")
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    plt.tight_layout()
    st.pyplot(fig_graph, use_container_width=True)

    st.caption(f"🏆 **Most Efficient:** `{most_efficient['algorithm']}` evaluated the fewest nodes ({most_efficient['nodes_explored']}).")
"""
Shortest Path Finding in a Maze - Streamlit Application
Wayfinder: 3-Panel Dashboard with Custom UI Polish & High-Contrast Visuals
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from maze.maze import Maze
from algorithms.bfs import solve_bfs
from algorithms.dijkstra import solve_dijkstra
from algorithms.astar import solve_astar
from algorithms.bellman_ford import solve_bellman_ford
from visualization.plotter import plot_maze, ALGO_COLORS

# Page Setup
st.set_page_config(
    page_title="Wayfinder",
    page_icon="🧩",
    layout="wide"
)

# Custom UI Polish & Card Styling
st.markdown("""
<style>
    /* Styled Panel Column Containers */
    div[data-testid="stColumn"] {
        background-color: #1A1D24;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #2E3440;
    }
    /* Button Customization */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
    }
    /* Subheader Alignment */
    h3 {
        padding-top: 0rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("Wayfinder")
    st.caption("Interactive Pathfinding & Maze Visualizer")
    st.divider()

    col_controls, col_maze, col_metrics = st.columns([1, 2, 1])

    # Ensure benchmark data state exists
    if "benchmark_data" not in st.session_state:
        st.session_state.benchmark_data = None

    # --- PANEL 1: CONTROLS ---
    with col_controls:
        st.subheader("CONTROLS")
        maze_size = st.selectbox("Maze Size", ["11x11", "21x21", "31x31"], index=2, key="sb_maze_size")
        size = int(maze_size.split("x")[0])

        st.write("**Select Algorithms to Compare:**")
        # Set value=False so checkboxes start unchecked by default
        use_bfs = st.checkbox("BFS", value=False, key="chk_bfs")
        use_dijkstra = st.checkbox("Dijkstra's", value=False, key="chk_dijkstra")
        use_astar = st.checkbox("A*", value=False, key="chk_astar")
        use_bellman = st.checkbox("Bellman-Ford", value=False, key="chk_bellman")

        st.write("")
        btn_generate = st.button("🎲 Generate Multi-Path Maze", use_container_width=True, key="btn_gen")
        btn_run = st.button("▶ Run Comparison", type="primary", use_container_width=True, key="btn_run")

    # Initialize or reset session maze instance
    if "maze" not in st.session_state or st.session_state.maze.rows != size:
        st.session_state.maze = Maze(rows=size, cols=size)
        st.session_state.benchmark_data = None

    maze = st.session_state.maze

    # Trigger multi-path braided maze generation
    if btn_generate:
        maze.generate_multipath_maze(braid_factor=0.35)
        st.session_state.benchmark_data = None
        st.rerun()

    # Execute selected algorithms ONLY when "Run Comparison" is clicked
    if btn_run:
        results = []
        if use_bfs:
            results.append(solve_bfs(maze))
        if use_dijkstra:
            results.append(solve_dijkstra(maze))
        if use_astar:
            results.append(solve_astar(maze))
        if use_bellman:
            results.append(solve_bellman_ford(maze))
        st.session_state.benchmark_data = results

    benchmark_data = st.session_state.benchmark_data

    # --- PANEL 2: MAZE VIEW ---
    with col_maze:
        st.subheader("MAZE VIEW")
        st.info(f"Grid Canvas: {maze.rows} × {maze.cols}")

        # Legend mapping active algorithm path colors
        if benchmark_data:
            legend_cols = st.columns(len(benchmark_data))
            for idx, res in enumerate(benchmark_data):
                algo = res["algorithm"]
                color = ALGO_COLORS.get(algo, "#FF2A6D")
                legend_cols[idx].markdown(
                    f"<span style='color:{color}; font-weight:bold; font-size:15px;'>━━ {algo}</span>", 
                    unsafe_allow_html=True
                )

        # Vector Maze Canvas
        fig_maze = plot_maze(maze, benchmark_data=benchmark_data)
        st.pyplot(fig_maze, use_container_width=True)

    # --- PANEL 3: BENCHMARKS & PERFORMANCE CHARTS ---
    with col_metrics:
        st.subheader("BENCHMARKS")
        if benchmark_data:
            # Metric Highlights
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

            # Performance Bar Charts
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

            # Graph 2: Execution Time (ms)
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
        else:
            st.write("Select algorithms and click **▶ Run Comparison** to evaluate benchmarks.")

if __name__ == "__main__":
    main()
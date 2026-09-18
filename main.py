import streamlit as st
from maze.maze import Maze
from algorithms.bfs import solve_bfs
from algorithms.dijkstra import solve_dijkstra
from algorithms.astar import solve_astar
from algorithms.bellman_ford import solve_bellman_ford
from visualization.plotter import plot_maze
from ui.components import inject_custom_css, render_gaming_title, render_legend, render_benchmarks

st.set_page_config(page_title="Wayfinder", page_icon="⚡", layout="wide")
inject_custom_css()

def main():
    # Gaming Title Header
    render_gaming_title()
    st.divider()

    col_controls, col_maze, col_metrics = st.columns([1, 2, 1])

    if "benchmark_data" not in st.session_state:
        st.session_state.benchmark_data = None

    # --- PANEL 1: CONTROLS ---
    with col_controls:
        st.subheader("CONTROLS")
        maze_size = st.selectbox("Maze Size", ["11x11", "21x21", "31x31"], index=2, key="sb_maze_size")
        size = int(maze_size.split("x")[0])

        st.write("**Select Algorithms to Compare:**")
        use_bfs = st.checkbox("BFS", value=False, key="chk_bfs")
        use_dijkstra = st.checkbox("Dijkstra's", value=False, key="chk_dijkstra")
        use_astar = st.checkbox("A*", value=False, key="chk_astar")
        use_bellman = st.checkbox("Bellman-Ford", value=False, key="chk_bellman")

        st.write("")
        btn_generate = st.button("🎲 GENERATE MULTI-PATH MAZE", use_container_width=True, key="btn_gen")
        btn_run = st.button("▶ RUN COMPARISON", type="primary", use_container_width=True, key="btn_run")

    if "maze" not in st.session_state or st.session_state.maze.rows != size:
        st.session_state.maze = Maze(rows=size, cols=size)
        st.session_state.benchmark_data = None

    maze = st.session_state.maze

    if btn_generate:
        maze.generate_multipath_maze(braid_factor=0.35)
        st.session_state.benchmark_data = None
        st.rerun()

    if btn_run:
        results = []
        if use_bfs: results.append(solve_bfs(maze))
        if use_dijkstra: results.append(solve_dijkstra(maze))
        if use_astar: results.append(solve_astar(maze))
        if use_bellman: results.append(solve_bellman_ford(maze))
        st.session_state.benchmark_data = results

    benchmark_data = st.session_state.benchmark_data

    # --- PANEL 2: MAZE VIEW ---
    with col_maze:
        st.subheader("GRID CANVAS")
        st.info(f"GRID RESOLUTION: {maze.rows} × {maze.cols}")
        if benchmark_data:
            render_legend(benchmark_data)
        fig_maze = plot_maze(maze, benchmark_data=benchmark_data)
        st.pyplot(fig_maze, use_container_width=True)

    # --- PANEL 3: BENCHMARKS ---
    with col_metrics:
        st.subheader("LIVE BENCHMARKS")
        if benchmark_data:
            render_benchmarks(benchmark_data)
        else:
            st.write("Select algorithms and click **▶ RUN COMPARISON** to start benchmarking.")

if __name__ == "__main__":
    main()
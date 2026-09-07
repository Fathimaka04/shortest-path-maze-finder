"""
Shortest Path Finding in a Maze - Streamlit Application
UI Layout Matching Wireframe Diagram
Live BFS Execution & Real-Time Metrics
Dual Algorithm Support (BFS & Dijkstra)
Tri-Algorithm Support (BFS, Dijkstra, A*)
Complete 4-Algorithm BFS,Dijkstra,A*,Bellmann_Ford
"""

import streamlit as st
from maze.maze import Maze
from algorithms.bfs import solve_bfs
from algorithms.dijkstra import solve_dijkstra
from algorithms.astar import solve_astar
from algorithms.bellman_ford import solve_bellman_ford

st.set_page_config(
    page_title="Maze Shortest-Path Visualizer",
    page_icon="🧩",
    layout="wide"
)

def main():
    st.title("Maze Shortest-Path Visualizer")
    st.caption("localhost:8501 — Multi-Algorithm Comparative Engine")
    st.divider()

    col_controls, col_maze, col_metrics = st.columns([1, 2, 1])

    # --- PANEL 1: CONTROLS ---
    with col_controls:
        st.subheader("CONTROLS")
        maze_size = st.selectbox("Maze Size", ["10x10", "20x20", "30x30"], index=0)
        size = int(maze_size.split("x")[0])

        st.write("**Algorithms:**")
        c1, c2 = st.columns(2)
        with c1:
            use_bfs = st.checkbox("BFS", value=True)
            use_astar = st.checkbox("A*", value=False)
        with c2:
            use_dijkstra = st.checkbox("Dijkstra's", value=False)
            use_bellman = st.checkbox("Bellman-Ford", value=False)

        st.write("")
        btn_run = st.button("▶ Run Search", type="primary", use_container_width=True)

    # Sync maze instance with UI grid selection
    if "maze" not in st.session_state or st.session_state.maze.rows != size:
        st.session_state.maze = Maze(rows=size, cols=size)

    maze = st.session_state.maze

    # Execute selected algorithm
    results = None
    if btn_run:
        if use_bellman:
            results = solve_bellman_ford(maze)
        elif use_astar:
            results = solve_astar(maze)
        elif use_dijkstra:
            results = solve_dijkstra(maze)
        elif use_bfs:
            results = solve_bfs(maze)

    # --- PANEL 2: MAZE VIEW ---
    with col_maze:
        st.subheader("MAZE VIEW")
        st.info(f"Grid Canvas: {maze.rows} × {maze.cols}")
        st.write(f"**Start Coordinate:** `{maze.start}` | **End Coordinate:** `{maze.end}`")

        if results and results["success"]:
            st.success(f"Path Found using {results['algorithm']}!")
            st.write("**Calculated Coordinate Path:**")
            st.code(f"{results['path']}")
        elif results and not results["success"]:
            st.error("No valid path exists between Start and End coordinates!")
        else:
            st.write("Click **▶ Run Search** to execute selected algorithm.")

    # --- PANEL 3: METRICS ---
    with col_metrics:
        st.subheader("METRICS")
        if results and results["success"]:
            st.metric(label="Path Length", value=f"{results['path_length']} steps")
            st.metric(label="Nodes Explored", value=f"{results['nodes_explored']} operations")
            st.metric(label="Time Taken", value=f"{results['execution_time_ms']} ms")
            st.metric(label="Space Used", value=f"{results['space_used']} tracked nodes")
        else:
            st.metric(label="Path Length", value="-")
            st.metric(label="Nodes Explored", value="-")
            st.metric(label="Time Taken", value="-")
            st.metric(label="Space Used", value="-")

if __name__ == "__main__":
    main()
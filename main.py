"""
Shortest Path Finding in a Maze - Streamlit Application
UI Layout Matching Wireframe Diagram
"""

import streamlit as st
from maze.maze import Maze, CellType

st.set_page_config(
    page_title="Maze Shortest-Path Visualizer",
    page_icon="🧩",
    layout="wide"
)

def main():
    st.title("Streamlit Application Design")
    st.caption("Maze Shortest-Path Visualizer")
    st.divider()

    # Create 3-Panel Grid Layout: [CONTROLS | MAZE VIEW | METRICS]
    col_controls, col_maze, col_metrics = st.columns([1, 2, 1])

    # --- PANEL 1: CONTROLS ---
    with col_controls:
        st.subheader("CONTROLS")
        
        maze_size = st.selectbox("Maze Size", ["10x10", "20x20", "30x30"], index=0)
        
        st.write("**Algorithms:**")
        c1, c2 = st.columns(2)
        with c1:
            use_bfs = st.checkbox("BFS", value=True)
            use_astar = st.checkbox("A*", value=True)
        with c2:
            use_dijkstra = st.checkbox("Dijkstra's", value=True)
            use_bellman = st.checkbox("Bellman-Ford", value=True)

        st.write("")
        btn_generate = st.button("▶ Generate Maze", use_container_width=True)
        btn_run = st.button("▶ Run Comparison", type="primary", use_container_width=True)

    # --- PANEL 2: MAZE VIEW ---
    with col_maze:
        st.subheader("MAZE VIEW")
        
        # Instantiate Maze based on selected size
        size = int(maze_size.split("x")[0])
        maze = Maze(rows=size, cols=size)
        
        # Display Grid Information Container
        st.info(f"Grid Canvas Rendered ({maze.rows} × {maze.cols})")
        st.write(f"**Start:** `{maze.start}` | **End:** `{maze.end}`")
        
        # Grid canvas placeholder (Interactive canvas will be integrated in Phase 3/4)
        st.success("Maze state initialized and ready for search execution!")

    # --- PANEL 3: METRICS ---
    with col_metrics:
        st.subheader("METRICS")
        
        st.metric(label="Path Length", value="-")
        st.metric(label="Nodes Explored", value="-")
        st.metric(label="Time Taken", value="-")
        st.metric(label="Space Used", value="-")

    # st.caption("Hand-sketched wireframe — final layout to be refined during implementation.")

if __name__ == "__main__":
    main()
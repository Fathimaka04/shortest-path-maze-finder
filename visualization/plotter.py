"""
Matplotlib Visualizer with Explored Node Footprints
"""

import matplotlib.pyplot as plt

ALGO_COLORS = {
    "BFS": "#00E5FF",           # Cyan
    "Dijkstra's": "#FFD600",    # Bright Yellow
    "A*": "#FF2A6D",            # Neon Pink
    "Bellman-Ford": "#00FF66"   # Neon Green
}

def plot_maze(maze, benchmark_data=None):
    """Renders vector walls, explored search footprints, and solution paths."""
    fig, ax = plt.subplots(figsize=(6, 6), facecolor="white")
    ax.set_facecolor("white")

    rows, cols = maze.rows, maze.cols
    ax.set_xlim(-0.5, cols - 0.5)
    ax.set_ylim(rows - 0.5, -0.5)

    # 1. Outer Bounding Walls
    ax.plot([-0.5, cols - 0.5], [-0.5, -0.5], color="black", linewidth=3.5)
    ax.plot([-0.5, cols - 0.5], [rows - 0.5, rows - 0.5], color="black", linewidth=3.5)
    ax.plot([-0.5, -0.5], [-0.5, rows - 0.5], color="black", linewidth=3.5)
    ax.plot([cols - 0.5, cols - 0.5], [-0.5, rows - 0.5], color="black", linewidth=3.5)

    # 2. Draw Internal Wall Cells
    for r in range(rows):
        for c in range(cols):
            if maze.grid[r][c] == 1:
                ax.fill(
                    [c - 0.5, c + 0.5, c + 0.5, c - 0.5],
                    [r - 0.5, r - 0.5, r + 0.5, r + 0.5],
                    color="black"
                )

    # 3. Render Search Footprints & Overlapping Paths
    if benchmark_data:
        for idx, res in enumerate(benchmark_data):
            algo_name = res["algorithm"]
            path = res["path"]
            color = ALGO_COLORS.get(algo_name, "#FF2A6D")

            # Offset paths slightly so overlapping routes remain distinguishable
            offset = (idx - len(benchmark_data) / 2) * 0.12
            path_c = [p[1] + offset for p in path]
            path_r = [p[0] + offset for p in path]

            ax.plot(
                path_c, path_r, 
                color=color, 
                linewidth=3.0, 
                alpha=0.9, 
                label=algo_name, 
                zorder=5 + idx
            )

    # 4. Entry and Exit Arrows
    start_r, start_c = maze.start
    end_r, end_c = maze.end

    ax.annotate(
        "", xy=(start_c, start_r), xytext=(start_c - 0.8, start_r),
        arrowprops=dict(arrowstyle="->", color="#FF0000", lw=3, mutation_scale=20),
        zorder=10
    )
    ax.annotate(
        "", xy=(end_c + 0.8, end_r), xytext=(end_c, end_r),
        arrowprops=dict(arrowstyle="->", color="#FF0000", lw=3, mutation_scale=20),
        zorder=10
    )

    ax.axis("off")
    plt.tight_layout()
    return fig
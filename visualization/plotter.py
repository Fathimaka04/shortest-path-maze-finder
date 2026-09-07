"""
Matplotlib High-Contrast Maze Renderer
Renders thin vector walls, crisp pathways, and start/end arrows.
"""

import matplotlib.pyplot as plt

def plot_maze(maze, path=None):
    """
    Renders the grid with thin black vector walls on a clean white canvas.
    """
    fig, ax = plt.subplots(figsize=(6, 6), facecolor="white")
    ax.set_facecolor("white")

    # Set grid limits based on dimensions
    rows, cols = maze.rows, maze.cols
    ax.set_xlim(-0.5, cols - 0.5)
    ax.set_ylim(rows - 0.5, -0.5)  # Invert Y to match grid (0,0 at top-left)

    # 1. Draw Outer Bounding Walls
    ax.plot([-0.5, cols - 0.5], [-0.5, -0.5], color="black", linewidth=3.5)  # Top
    ax.plot([-0.5, cols - 0.5], [rows - 0.5, rows - 0.5], color="black", linewidth=3.5)  # Bottom
    ax.plot([-0.5, -0.5], [-0.5, rows - 0.5], color="black", linewidth=3.5)  # Left
    ax.plot([cols - 0.5, cols - 0.5], [-0.5, rows - 0.5], color="black", linewidth=3.5)  # Right

    # 2. Draw Internal Wall Cells as Crisp Line Segments
    for r in range(rows):
        for c in range(cols):
            if maze.grid[r][c] == 1:  # Wall cell
                # Draw square boundary around the wall cell
                ax.fill(
                    [c - 0.5, c + 0.5, c + 0.5, c - 0.5],
                    [r - 0.5, r - 0.5, r + 0.5, r + 0.5],
                    color="black"
                )

    # 3. Plot Solution Path
    if path:
        path_c = [p[1] for p in path]
        path_r = [p[0] for p in path]
        ax.plot(path_c, path_r, color="#FF2A6D", linewidth=3.5, linestyle="-", zorder=4)

    # 4. Draw Red Entry/Exit Directional Arrows
    start_r, start_c = maze.start
    end_r, end_c = maze.end

    # Start Arrow (Pointing Right into Start)
    ax.annotate(
        "", xy=(start_c, start_r), xytext=(start_c - 0.8, start_r),
        arrowprops=dict(arrowstyle="->", color="#FF0000", lw=3, mutation_scale=20),
        zorder=5
    )
    # End Arrow (Pointing Right out of End)
    ax.annotate(
        "", xy=(end_c + 0.8, end_r), xytext=(end_c, end_r),
        arrowprops=dict(arrowstyle="->", color="#FF0000", lw=3, mutation_scale=20),
        zorder=5
    )

    # Remove axes ticks and borders for clean presentation output
    ax.axis("off")
    plt.tight_layout()
    
    return fig
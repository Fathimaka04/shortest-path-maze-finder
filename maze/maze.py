"""
Maze Data Structure & Generator Engine
Supports single-path classic mazes and multi-path braided mazes.
"""

import random

class CellType:
    EMPTY = 0
    WALL = 1

class Maze:
    def __init__(self, rows=11, cols=11):
        self.rows = rows
        self.cols = cols
        self.grid = [[CellType.EMPTY for _ in range(cols)] for _ in range(rows)]
        self.costs = [[1 for _ in range(cols)] for _ in range(rows)]
        self.start = (0, 0)
        self.end = (rows - 1, cols - 1)

    def generate_random_maze(self):
        """Generates a classic single-solution vector maze using Recursive Backtracking (DFS)."""
        self.grid = [[CellType.WALL for _ in range(self.cols)] for _ in range(self.rows)]
        self.costs = [[1 for _ in range(self.cols)] for _ in range(self.rows)]
        
        stack = [(0, 0)]
        self.grid[0][0] = CellType.EMPTY
        visited = {(0, 0)}

        while stack:
            r, c = stack[-1]
            neighbors = []

            for dr, dc in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in visited:
                    neighbors.append((nr, nc, r + dr // 2, c + dc // 2))

            if neighbors:
                next_r, next_c, wall_r, wall_c = random.choice(neighbors)
                self.grid[wall_r][wall_c] = CellType.EMPTY
                self.grid[next_r][next_c] = CellType.EMPTY
                visited.add((next_r, next_c))
                stack.append((next_r, next_c))
            else:
                stack.pop()

        self.start = (0, 0)
        self.end = (self.rows - 1, self.cols - 1)
        self.grid[self.start[0]][self.start[1]] = CellType.EMPTY
        self.grid[self.end[0]][self.end[1]] = CellType.EMPTY

    def generate_multipath_maze(self, braid_factor=0.35):
        """
        Generates a braided maze with multiple interconnected paths and loops.
        braid_factor: Percentage of internal wall junctions to remove (0.0 to 1.0)
        """
        # Step 1: Generate a baseline spanning maze via DFS
        self.generate_random_maze()

        # Step 2: Knock down extra internal wall blocks to create competing routes
        for r in range(1, self.rows - 1):
            for c in range(1, self.cols - 1):
                if self.grid[r][c] == CellType.WALL:
                    # Check if wall separates two open paths
                    if (self.grid[r-1][c] == CellType.EMPTY and self.grid[r+1][c] == CellType.EMPTY) or \
                       (self.grid[r][c-1] == CellType.EMPTY and self.grid[r][c+1] == CellType.EMPTY):
                        if random.random() < braid_factor:
                            self.grid[r][c] = CellType.EMPTY

        # Ensure start and end remain open
        self.start = (0, 0)
        self.end = (self.rows - 1, self.cols - 1)
        self.grid[self.start[0]][self.start[1]] = CellType.EMPTY
        self.grid[self.end[0]][self.end[1]] = CellType.EMPTY

    def get_neighbors(self, pos):
        """Returns valid adjacent moves (Up, Down, Left, Right) along with movement costs."""
        r, c = pos
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] != CellType.WALL:
                    cost = self.costs[nr][nc]
                    neighbors.append(((nr, nc), cost))

        return neighbors
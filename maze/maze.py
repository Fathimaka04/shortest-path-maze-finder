"""
Maze Data Structure & Recursive Backtracking Maze Generator
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
        """Generates a classic maze using Recursive Backtracking (DFS)."""
        # Fill everything with walls initially
        self.grid = [[CellType.WALL for _ in range(self.cols)] for _ in range(self.rows)]
        self.costs = [[1 for _ in range(self.cols)] for _ in range(self.rows)]
        
        # Start carving paths from (0,0)
        stack = [(0, 0)]
        self.grid[0][0] = CellType.EMPTY
        visited = {(0, 0)}

        while stack:
            r, c = stack[-1]
            neighbors = []

            # Check moves 2 steps away to leave wall borders
            for dr, dc in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in visited:
                    neighbors.append((nr, nc, r + dr // 2, c + dc // 2))

            if neighbors:
                # Pick a random neighbor and carve a passage through the wall
                next_r, next_c, wall_r, wall_c = random.choice(neighbors)
                self.grid[wall_r][wall_c] = CellType.EMPTY
                self.grid[next_r][next_c] = CellType.EMPTY
                visited.add((next_r, next_c))
                stack.append((next_r, next_c))
            else:
                stack.pop()

        # Ensure Start and End coordinates are open passages
        self.start = (0, 0)
        self.end = (self.rows - 1, self.cols - 1)
        self.grid[self.start[0]][self.start[1]] = CellType.EMPTY
        self.grid[self.end[0]][self.end[1]] = CellType.EMPTY

    def get_neighbors(self, pos):
        """
        Returns valid adjacent moves (Up, Down, Left, Right) from position pos (r, c)
        along with edge costs.
        """
        r, c = pos
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] != CellType.WALL:
                    cost = self.costs[nr][nc]
                    neighbors.append(((nr, nc), cost))

        return neighbors
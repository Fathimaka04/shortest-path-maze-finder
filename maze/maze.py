"""
Mmaze Representation and Grid Graph Data Structure

"""

class CellType:
    """Cell status codes for grid elements."""
    EMPTY = 0
    WALL = 1

class Maze:
    """
    Represents a 2D grid maze and provides graph neighbor lookup functionalities.
    """
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        
        # Grid stores cell types: 0 for empty, 1 for wall
        self.grid = [[CellType.EMPTY for _ in range(cols)] for _ in range(rows)]
        
        # Costs grid: default cost is 1 for open cells
        self.costs = [[1 for _ in range(cols)] for _ in range(rows)]
        
        # Start and End positions as (row, col) tuples
        self.start = (0, 0)
        self.end = (rows - 1, cols - 1)

    def set_wall(self, row, col):
        """Sets a cell as a wall if it is not start or end."""
        if (row, col) != self.start and (row, col) != self.end:
            self.grid[row][col] = CellType.WALL

    def remove_wall(self, row, col):
        """Clears a wall, making it an empty cell."""
        self.grid[row][col] = CellType.EMPTY

    def set_cell_cost(self, row, col, cost):
        """Assigns a movement cost to a specific cell."""
        if cost > 0:
            self.costs[row][col] = cost

    def is_valid(self, row, col):
        """Checks if a cell coordinate is within grid bounds and not a wall."""
        is_in_bounds = 0 <= row < self.rows and 0 <= col < self.cols
        if not is_in_bounds:
            return False
        return self.grid[row][col] != CellType.WALL

    def get_neighbors(self, node):
        """
        Returns valid adjacent 4-directional neighbors (UP, DOWN, LEFT, RIGHT)
        along with their step movement costs.
        
        Returns:
            list of tuples: [((neighbor_row, neighbor_col), edge_cost), ...]
        """
        r, c = node
        # 4-Directional movements: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if self.is_valid(nr, nc):
                edge_cost = self.costs[nr][nc]
                neighbors.append(((nr, nc), edge_cost))

        return neighbors

    def reset_grid(self):
        """Resets walls and cell costs back to default empty grid."""
        self.grid = [[CellType.EMPTY for _ in range(self.cols)] for _ in range(self.rows)]
        self.costs = [[1 for _ in range(self.cols)] for _ in range(self.rows)]
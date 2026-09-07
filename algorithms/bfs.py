"""
Breadth-First Search (BFS) Algorithm Implementation
Phase 3: Uninformed Search Engine
"""

from collections import deque
import time

def solve_bfs(maze):
    """
    Executes BFS to find the shortest path in an unweighted grid.
    
    Returns:
        dict: Benchmarking results including path, path length, nodes explored, 
              execution time (ms), and peak space used.
    """
    start_time = time.perf_counter()
    
    start = maze.start
    end = maze.end
    
    # FIFO Queue stores tuples of (current_node, path_taken)
    queue = deque([(start, [start])])
    
    # Set to track visited coordinates
    visited = {start}
    
    nodes_explored = 0
    max_queue_size = 1  # Tracks peak space complexity

    path_found = None

    while queue:
        # Track maximum space used by queue
        max_queue_size = max(max_queue_size, len(queue))
        
        current, path = queue.popleft()
        nodes_explored += 1

        # Goal check
        if current == end:
            path_found = path
            break

        # Explore 4-directional neighbors
        for neighbor, _ in maze.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds

    return {
        "algorithm": "BFS",
        "path": path_found,
        "path_length": len(path_found) - 1 if path_found else 0,
        "nodes_explored": nodes_explored,
        "execution_time_ms": round(execution_time_ms, 3),
        "space_used": max_queue_size,
        "success": path_found is not None
    }
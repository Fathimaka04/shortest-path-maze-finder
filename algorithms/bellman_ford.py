"""
Bellman-Ford Algorithm Implementation
Phase 6: Dynamic Programming Search Engine
"""

import time

def solve_bellman_ford(maze):
    """
    Executes the Bellman-Ford algorithm over the grid graph via iterative edge relaxation.
    
    Returns:
        dict: Benchmarking results including path, total path cost, 
              nodes explored, execution time (ms), and space usage.
    """
    start_time = time.perf_counter()
    
    start = maze.start
    end = maze.end
    
    # 1. Extract all traversable cells (Vertices)
    vertices = []
    for r in range(maze.rows):
        for c in range(maze.cols):
            if maze.grid[r][c] != 1:  # Not a wall
                vertices.append((r, c))
                
    if start not in vertices or end not in vertices:
        return {"algorithm": "Bellman-Ford", "success": False}

    # 2. Distance and predecessor tracking
    distances = {v: float('inf') for v in vertices}
    predecessors = {v: None for v in vertices}
    distances[start] = 0

    nodes_explored = 0

    # 3. Main Relaxation Loop: Repeat (V - 1) times
    num_vertices = len(vertices)
    for _ in range(num_vertices - 1):
        relaxed_any = False
        
        for u in vertices:
            # Only relax edges from reachable nodes
            if distances[u] == float('inf'):
                continue
                
            nodes_explored += 1
            for v, weight in maze.get_neighbors(u):
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
                    relaxed_any = True
                    
        # Early termination optimization if no distances changed in a full pass
        if not relaxed_any:
            break

    # 4. Reconstruct Path from Target
    path_found = []
    curr = end
    if distances[end] != float('inf'):
        while curr is not None:
            path_found.append(curr)
            curr = predecessors[curr]
        path_found.reverse()

    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000

    return {
        "algorithm": "Bellman-Ford",
        "path": path_found if path_found else None,
        "path_length": distances[end] if distances[end] != float('inf') else 0,
        "nodes_explored": nodes_explored,
        "execution_time_ms": round(execution_time_ms, 3),
        "space_used": len(vertices),  # Vertices array space overhead
        "success": len(path_found) > 0
    }
"""
A* Search Algorithm Implementation
Phase 5: Heuristic-Driven Informed Search Engine
"""

import heapq
import time

def manhattan_distance(p1, p2):
    """Calculates Manhattan distance heuristic between two coordinates (r1, c1) and (r2, c2)."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve_astar(maze):
    """
    Executes A* Search using a Priority Queue (Min-Heap) and Manhattan Distance heuristic.
    
    Returns:
        dict: Benchmarking results including path, total path cost, 
              nodes explored, execution time (ms), and peak priority queue size.
    """
    start_time = time.perf_counter()
    
    start = maze.start
    end = maze.end
    
    # Priority Queue stores tuples of (f_score, current_cost_g, current_node, path_taken)
    # f(n) = g(n) + h(n)
    h_start = manhattan_distance(start, end)
    pq = [(h_start, 0, start, [start])]
    
    # Track lowest known g(n) cost to reach each node
    g_scores = {start: 0}
    visited = set()
    
    nodes_explored = 0
    max_pq_size = 1

    path_found = None
    final_cost = 0

    while pq:
        max_pq_size = max(max_pq_size, len(pq))
        
        f_score, g_score, current, path = heapq.heappop(pq)

        if current in visited:
            continue
            
        visited.add(current)
        nodes_explored += 1

        # Goal check
        if current == end:
            path_found = path
            final_cost = g_score
            break

        # Explore neighbors
        for neighbor, edge_cost in maze.get_neighbors(current):
            tentative_g = g_score + edge_cost
            
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_neighbor = tentative_g + manhattan_distance(neighbor, end)
                heapq.heappush(pq, (f_neighbor, tentative_g, neighbor, path + [neighbor]))

    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000

    return {
        "algorithm": "A*",
        "path": path_found,
        "path_length": final_cost,
        "nodes_explored": nodes_explored,
        "execution_time_ms": round(execution_time_ms, 3),
        "space_used": max_pq_size,
        "success": path_found is not None
    }
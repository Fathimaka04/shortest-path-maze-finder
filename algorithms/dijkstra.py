"""
Dijkstra's Algorithm Implementation
Phase 4: Weighted Uniform-Cost Search Engine
"""

import heapq
import time

def solve_dijkstra(maze):
    """
    Executes Dijkstra's algorithm using a Priority Queue (Min-Heap).
    
    Returns:
        dict: Benchmarking results including path, total path cost, 
              nodes explored, execution time (ms), and max priority queue size.
    """
    start_time = time.perf_counter()
    
    start = maze.start
    end = maze.end
    
    # Priority Queue stores tuples of (cumulative_cost, current_node, path_taken)
    pq = [(0, start, [start])]
    
    # Dictionary tracking lowest known cost to reach each node
    distances = {start: 0}
    visited = set()
    
    nodes_explored = 0
    max_pq_size = 1

    path_found = None
    final_cost = 0

    while pq:
        max_pq_size = max(max_pq_size, len(pq))
        
        current_cost, current, path = heapq.heappop(pq)

        if current in visited:
            continue
            
        visited.add(current)
        nodes_explored += 1

        # Goal check
        if current == end:
            path_found = path
            final_cost = current_cost
            break

        # Explore neighbors and relax edges
        for neighbor, edge_cost in maze.get_neighbors(current):
            new_cost = current_cost + edge_cost
            
            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))

    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000

    return {
        "algorithm": "Dijkstra's",
        "path": path_found,
        "path_length": final_cost,
        "nodes_explored": nodes_explored,
        "execution_time_ms": round(execution_time_ms, 3),
        "space_used": max_pq_size,
        "success": path_found is not None
    }
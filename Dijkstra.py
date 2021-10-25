from collections import defaultdict
import heapq
def Dijkstra(edgelist, start_node):
    
    graph = defaultdict(list)
    for a, b, v in edgelist:
        # undirected graph, both way works
        if v > 0: # v == 0 means no edge or weigh is inf
            graph[a].append((b, v))
            graph[b].append((a, v))

    distance = {node:float('inf') for node in graph}
    distance[start_node] = 0
    visited = set()
    heap = []
    heapq.heappush(heap, (0, start_node))
    while heap:
        d, node = heapq.heappop(heap)
        visited.add(node)

        # relaxation on children of node
        for child, weight in graph[node]:
            if child not in visited:
                distance[child] = min(d + weight, distance[child])
                heapq.heappush(heap, (distance[child], child))
            
    return distance

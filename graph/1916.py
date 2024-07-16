import heapq
import sys

def town(graph, start, n):
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        
        if current_distance > dist[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return dist

n = int(input().strip())
m = int(input().strip())

graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c))
    
start, end = map(int, input().split())

distances = town(graph, start, n)

print(distances[end])
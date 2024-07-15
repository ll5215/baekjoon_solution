from collections import deque
import sys


n, m, v = map(int, sys.stdin.readline().split())

def dfs(graph, vertex, visited = None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex,end = ' ')
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            queue.extend([neighbor for neighbor in graph[vertex] if neighbor not in visited])
    return visited
    
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for key in graph:
    graph[key].sort()
    
dfs(graph, v)
print()

bfs(graph, v)
print()
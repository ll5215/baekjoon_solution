import sys


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(graph, vertex, visited = None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

count = len(dfs(graph,1))
print(count - 1)
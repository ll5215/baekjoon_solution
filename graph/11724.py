import sys
    
def dfs(graph, vertex, visited):
    visited.add(vertex)
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            
n, m = map(int, sys.stdin.readline().split())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
            
visited = set()
count = 0

for i in range(1, n+1):
    if i not in visited:
        dfs(graph, i, visited)
        count += 1
        
print(count)

        
import sys

def dfs(graph, start, parents):
    stack = [start]
    while stack:
        vertex = stack.pop()
        for neighbor in graph[vertex]:
            if parents[vertex] != neighbor:
                parents[neighbor] = vertex
                stack.append(neighbor)

n = int(sys.stdin.readline())
    
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [0] * (n + 1)
dfs(graph, 1, parents)

for i in range(2, n + 1):
    print(parents[i])
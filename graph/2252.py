from collections import deque


def topological(graph):
    in_degree = {u:0 for u in graph}
    
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque([u for u in graph if in_degree[u] == 0])
    top_order = []
    
    while queue:
        u = queue.popleft()
        top_order.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    if len(top_order) == len(graph):
        return top_order
    else: 
        return []


n ,m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
for i in range(m):
    a, b = (map(int, input().split()))
    graph[a].append(b)
    
result = topological(graph)
if result:
    print(" ".join(map(str, result)))
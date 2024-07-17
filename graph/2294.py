from collections import deque
import sys

def coin_bfs(graph, k):
    queue = deque([(0, 0)])
    visited = [False] * (k + 1)
    visited[0] = True

    while queue:
        amount, coin_count = queue.popleft()

        for coin in graph:
            next_amount = amount + coin

            if next_amount == k:
                return coin_count + 1

            if next_amount <= k and not visited[next_amount]:
                visited[next_amount] = True
                queue.append((next_amount, coin_count + 1))

    return -1

n, k = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(int(sys.stdin.readline()))

print(coin_bfs(graph, k))

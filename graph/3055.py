from collections import deque
import sys

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def save_hedgehog(r, c, graph):
    water_queue = deque()
    hedgehog_queue = deque()
    visited = [[False] * c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '*':
                water_queue.append((i, j))
            elif graph[i][j] == 'S':
                hedgehog_queue.append((i, j, 0))
                visited[i][j] = True
                
    while water_queue or hedgehog_queue:
        water_len = len(water_queue)
        for _ in range(water_len):
            x, y = water_queue.popleft()
            for dx, dy in directions:
                nx, ny = x +dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    water_queue.append((nx, ny))
                    
        hedgehog_len = len(hedgehog_queue)
        for _ in range(hedgehog_len):
            x, y, steps = hedgehog_queue.popleft()
            for dx, dy in directions:
                nx, ny = x +dx, y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == 'D':
                        return steps + 1
                    if graph[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        hedgehog_queue.append((nx, ny, steps + 1))
    return "KAKTUS"


r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(r)]
    
print(save_hedgehog(r, c, graph))
from collections import deque

def bfs():
    while queue:
        virus, s, x, y = queue.popleft()
        if s == S:
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0:
                grid[nx][ny] = virus
                queue.append((virus, s + 1, nx, ny))

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

queue = deque()

# 초기 바이러스 상태 저장
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            queue.append((grid[i][j], 0, i, j))

# 바이러스 번호가 낮은 순으로 정렬
queue = deque(sorted(queue))

# BFS를 이용한 전염 시뮬레이션
bfs()

# 결과 출력
print(grid[X-1][Y-1])

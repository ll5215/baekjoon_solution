def dfs(x, y):
    # Stack for DFS
    stack = [(x, y)]
    count = 0
    while stack:
        cx, cy = stack.pop()
        if 0 <= cx < N and 0 <= cy < N and not visited[cx][cy] and grid[cx][cy] == '1':
            visited[cx][cy] = True
            count += 1
            # 상하좌우 네 방향을 탐색
            stack.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])
    return count

N = int(input())
grid = [input().strip() for _ in range(N)]
visited = [[False] * N for _ in range(N)]

num_of_complexes = 0
complex_sizes = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == '1' and not visited[i][j]:
            complex_size = dfs(i, j)
            if complex_size > 0:
                complex_sizes.append(complex_size)
                num_of_complexes += 1

# 결과 출력
print(num_of_complexes)
for size in sorted(complex_sizes):
    print(size)

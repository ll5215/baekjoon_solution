def dfs(x, y, char):
    # char가 '-'인 경우 가로로 이동
    if char == '-':
        while y < M and floor[x][y] == '-':
            visited[x][y] = True  # 현재 위치 방문 처리
            y += 1  # 다음 열로 이동
    # char가 '|'인 경우 세로로 이동
    elif char == '|':
        while x < N and floor[x][y] == '|':
            visited[x][y] = True  # 현재 위치 방문 처리
            x += 1  # 다음 행으로 이동

# N과 M을 입력 받음
N, M = map(int, input().split())
# 바닥 장식 상태를 입력 받음
floor = [input().strip() for _ in range(N)]
# 방문 체크 배열 초기화
visited = [[False] * M for _ in range(N)]

count = 0  # 장식 블록 수 카운트
# 모든 칸을 순회하면서 방문하지 않은 곳을 탐색
for i in range(N):
    for j in range(M):
        if not visited[i][j]:  # 방문하지 않은 경우
            dfs(i, j, floor[i][j])  # DFS 수행
            count += 1  # 블록 수 증가

# 결과 출력
print(count)

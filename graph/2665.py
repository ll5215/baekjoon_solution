import heapq

def min_black_rooms(n, grid):
    # 4가지 방향 (상, 하, 좌, 우) 이동을 위한 델타값 설정
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 방문 여부를 기록할 2차원 리스트 초기화
    visited = [[False] * n for _ in range(n)]
    
    # 우선순위 큐를 초기화하고 시작 지점 (0, 0)에서 출발
    # (검은 방의 수, x좌표, y좌표) 형태로 큐에 넣음
    pq = [(0, 0, 0)]
    heapq.heapify(pq)
    
    # 우선순위 큐가 비어있지 않은 동안 반복
    while pq:
        # 큐에서 현재 위치와 검은 방의 수를 꺼냄
        black_rooms, x, y = heapq.heappop(pq)
        
        # 이미 방문한 위치라면 건너뜀
        if visited[x][y]:
            continue
        
        # 현재 위치를 방문 처리
        visited[x][y] = True
        
        # 목표 지점 (n-1, n-1)에 도착했으면 검은 방의 수를 반환
        if x == n - 1 and y == n - 1:
            return black_rooms
        
        # 4가지 방향으로 이동 시도
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 새로운 위치가 미로 범위 내에 있고 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 다음 위치가 검은 방이면 검은 방의 수를 1 증가
                next_black_rooms = black_rooms + (1 if grid[nx][ny] == 0 else 0)
                # 다음 위치와 검은 방의 수를 우선순위 큐에 추가
                heapq.heappush(pq, (next_black_rooms, nx, ny))

# 입력을 받아 미로의 크기와 미로의 상태를 저장
n = int(input())  # 미로의 크기
grid = [list(map(int, input().strip())) for _ in range(n)]  # 미로 상태 (0은 검은 방, 1은 하얀 방)
# 최소 검은 방의 수를 출력
print(min_black_rooms(n, grid))

from collections import deque 

n, m, h = map(int,input().split()) # n, m, h에 대한 입력을 받음

graph = [] # 3차원 list 생성 
for _ in range(h):
    layer = []
    for i in range(m): # m개의 rows에 대해서 map에 대한 정보를 얻음
        layer.append(list(map(int,input().split()))) #row들을 layer에 추가
    graph.append(layer) # layer를 그래프에 추가

# 위,아래,오른쪽,왼쪽,앞,뒤 6방향으로 움직이도록 하는 lists
dx = [-1,1,0,0,0,0] 
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(x,y,z): # BFS 선언, 입력으로 x, y, z의 정보를 받음
    queue = deque() # queue 초기화
    
     # 익은 토마토 위치를 모두 큐에 삽입
    for z in range(h):  # 높이(층)를 나타내는 반복문
        for y in range(m):  # 행을 나타내는 반복문
            for x in range(n):  # 열을 나타내는 반복문
                if graph[z][y][x] == 1:  # 현재 위치에 익은 토마토가 있다면
                    queue.append((x,y,z))   # 그 위치를 큐에 삽입


     # 큐에 있는 모든 익은 토마토를 기준으로 BFS를 수행하여 토마토를 익힘
    while queue:
        x, y, z = queue.popleft() # queue에서 꺼내기

        for i in range(6): # 6 방향에 대해서 이동 check
            nx = x+ dx[i] 
            ny = y+ dy[i]
            nz = z+ dz[i]

            # 이동한 위치가 범위 내에 있고, 아직 익지 않은 토마토라면
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1      # 현재 위치까지의 일수 +1을 기록
                queue.append((nx, ny, nz))    # 새로운 위치를 큐에 삽입
        
    
    # 모든 토마토가 익는 데 걸리는 최대 일수를 계산        
    max_days = 0
    for layer in graph:
        for row in layer:
            for value in row:
                if value == 0:  # 익지 않은 토마토가 있다면
                    return -1
                max_days = max( max_days, value)

    return max_days -1   # 처음 시작을 1로 했기 때문에 1을 빼줌

print(bfs(0,0,0))
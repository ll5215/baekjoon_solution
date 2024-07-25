def jump_game(n, board): 
    dp = [[0] * n for _ in range(n)]  #dp테이블 만들기
    dp[0][0] = 1  #시작지점
    
    for i in range(n):
        for j in range(n):
            if dp[i][j] != 0 and board[i][j] != 0:  #현재 위치 보드판 안에 있는지
                jump = board[i][j]  
                if i + jump < n:   #아래 칸이 보드판 안넘어가면
                    dp[i + jump][j] += dp[i][j]  #아래로 이동
                if j + jump < n:   #오른쪽 칸이 보드판 안넘어가면
                    dp[i][j + jump] += dp[i][j]   #오른쪽으로 이동
    return dp[n-1][n-1]

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

print(jump_game(n, board))
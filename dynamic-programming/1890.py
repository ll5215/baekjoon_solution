def solve_jump_game(n, board):
    # DP 테이블 초기화
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1  # 시작점

    # DP 테이블 채우기
    for i in range(n):
        for j in range(n):
            if dp[i][j] != 0 and board[i][j] != 0:  # 현재 칸이 도달 가능한 칸인지 확인
                jump = board[i][j]
                if i + jump < n:  # 아래쪽으로 이동
                    dp[i + jump][j] += dp[i][j]
                if j + jump < n:  # 오른쪽으로 이동
                    dp[i][j + jump] += dp[i][j]

    return dp[n-1][n-1]

import sys
input = sys.stdin.readline

# 입력 받기
n = int(input().strip())
board = [list(map(int, input().strip().split())) for _ in range(n)]

# 결과 출력
print(solve_jump_game(n, board))

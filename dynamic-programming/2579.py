import sys
input = sys.stdin.readline

# 계단의 개수를 입력받습니다.
n = int(input().strip())

# 각 계단의 점수를 저장할 리스트를 초기화합니다.
score = [0] * n

# 계단의 점수를 입력받아 리스트에 저장합니다.
for i in range(n):
    score[i] = int(input().strip())

# 계단이 1개인 경우, 그 계단의 점수가 최댓값이 됩니다.
if n == 1:
    print(score[0])
    sys.exit()

# 계단이 2개인 경우, 첫 번째 계단과 두 번째 계단의 점수를 더한 값이 최댓값이 됩니다.
elif n == 2:
    print(score[0] + score[1])
    sys.exit()

# dp 리스트를 초기화합니다. dp[i]는 i번째 계단까지의 최대 점수를 의미합니다.
dp = [0] * n

# 초기값을 설정합니다.
dp[0] = score[0]  # 첫 번째 계단의 점수는 그 계단의 점수와 같습니다.
dp[1] = score[0] + score[1]  # 두 번째 계단의 점수는 첫 번째 계단과 두 번째 계단의 점수를 더한 값입니다.
dp[2] = max(score[0] + score[2], score[1] + score[2])  # 세 번째 계단의 점수는 첫 번째와 세 번째 계단을 밟는 경우와 두 번째와 세 번째 계단을 밟는 경우 중 최대값입니다.

# 동적 계획법을 이용하여 각 계단까지의 최대 점수를 계산합니다.
for i in range(3, n):
    # i번째 계단까지의 최대 점수는 두 가지 경우 중 최대값입니다.
    # 1. i-2번째 계단에서 i번째 계단으로 오는 경우 (dp[i-2] + score[i])
    # 2. i-3번째 계단에서 i-1번째 계단을 밟고 i번째 계단으로 오는 경우 (dp[i-3] + score[i-1] + score[i])
    dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

# 마지막 계단까지의 최대 점수를 출력합니다.
print(dp[n-1])

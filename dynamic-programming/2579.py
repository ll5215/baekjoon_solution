import sys


n = int(sys.stdin.readline().strip())

score = [0] * n  #계단 점수
 
for i in range(n):
    score[i] = int(sys.stdin.readline().strip())  

#계단이 1개나 2개이면 그 계단의 점수가 최대값
if n == 1: 
    print(score[0])  
    sys.exit()
elif n == 2:  
    print(score[0] + score[1]) 
    sys.exit()
    
dp = [0] * n  #dp테이블

dp[0] = score[0]  #계단 1개면 그 계단 점수
dp[1] = score[0] + score[1]  #계단 2개면 1번이랑 2번 계단 더한 점수
dp[2] = max(score[0] + score[2], score[1] + score[2])  #계단 3개면 1번+3번 / 2번+3번 중 최댓값

for i in range(3, n):  #계단은 4번째부터 시작
    dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])  #점화식
    
print(dp[n-1])
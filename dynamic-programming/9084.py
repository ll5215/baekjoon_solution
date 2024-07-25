def num_ways_to_make_amount(coins, amount):
    # dp[i]는 금액 i를 만들 수 있는 방법의 수를 나타냅니다.
    dp = [0] * (amount + 1)
    
    # 0원을 만드는 방법은 아무 동전도 사용하지 않는 방법 하나뿐입니다.
    dp[0] = 1
    
    # 각 동전에 대해 순회합니다.
    for coin in coins:
        # 현재 동전으로 만들 수 있는 모든 금액을 업데이트합니다.
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    # 최종적으로 dp[amount]가 우리가 원하는 금액을 만드는 방법의 수가 됩니다.
    return dp[amount]

# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

# 테스트 케이스의 수
t = int(data[0])
index = 1

for _ in range(t):
    # 동전의 종류 수
    n = int(data[index])
    
    # 동전의 종류들
    coins = list(map(int, data[index + 1:index + 1 + n]))
    
    # 목표 금액
    amount = int(data[index + 1 + n])
    
    # 인덱스를 다음 테스트 케이스로 이동
    index += 2 + n
    
    # 주어진 동전들로 목표 금액을 만드는 경우의 수 출력
    print(num_ways_to_make_amount(coins, amount))

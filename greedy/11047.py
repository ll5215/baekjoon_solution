def coin_greedy(coins, k):
    coins.sort(reverse=True)  # 큰 값의 동전부터 사용하기 위해 내림차순 정렬
    count = 0

    for coin in coins:
        if k == 0:
            break
        count += k // coin  # 현재 동전으로 만들 수 있는 최대 개수 추가
        k %= coin  # 나머지 금액 업데이트

    if k > 0:
        return -1  # 목표 금액을 만들 수 없는 경우
    return count

import sys

n, k = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for _ in range(n)]

print(coin_greedy(coins, k))

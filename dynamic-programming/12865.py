def knapsack(weights, values, t):
    n = len(weights) 
    dp = [[0] * (t + 1) for _ in range(n + 1)]  

    for i in range(1, n + 1):
        for w in range(1, t + 1):
            if weights[i - 1] > w:  
                dp[i][w] = dp[i-1][w]  
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1]) 

    return dp[n][t]

t, n = map(int, input().split())
weights = []
values = []

for _ in range(t):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

weights = list(weights)
values = list(values)

print(knapsack(weights, values, n))  


# 입력 받는거 컨프리헨션 (zip 사용)

# t, n = map(int, input().split())
# weights, values = zip(*(map(int, input().split()) for _ in range(t)))

# weights = list(weights)
# values = list(values)
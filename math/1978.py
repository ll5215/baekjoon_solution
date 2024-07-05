N = int(input())
S = list(map(int, input().split()))
result = 0

for i in range(N):
    k = S[i]
    l = []
    for j in range(k):
        if k%(j+1) == 0:
            l.append(j+1)
        if len(l) == 2:
            result += 1
print(result)
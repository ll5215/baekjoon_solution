def calc(a,b,c):
    if b == 1:
        return a % c
    else:
        n = calc(a, b//2, c)
        if b % 2 == 0:
            return (n * n) % c
        else:
            return (n * n * a) % c
    
A, B, C = map(int, input().split())

print(calc(A, B, C))

# 지수법칙과 나머지 분배의 법칙을 이용해야한다. 아니면 런타임 에러.
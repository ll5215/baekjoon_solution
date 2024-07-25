def fib_iterative(n):
    if n <=1:
        return n
    a,b = 0,1
    for _ in range(2, n+2):
        a,b = b, (a+b) % 15746
    return b

n = int(input())
print(fib_iterative(n))
def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            return False
    return True

for t in range(int(input())):
    number = int(input())
    a, b = number//2, number//2
    while a > 0:
        if prime(a) and prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
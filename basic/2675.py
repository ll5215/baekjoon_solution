t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    n = len(s)
    for a in range(N):
        for r in range(r):
            print(s[a], end = "")
    print()
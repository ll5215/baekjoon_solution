T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    N = len(S)
    for a in range(N):
        for r in range(R):
            print(S[a], end = "")
    print()
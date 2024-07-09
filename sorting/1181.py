t = int(input())
arr = []

for i in range(t):
    arr.append(input())

arr = set(arr)
arr = list(arr)

arr.sort()

arr.sort(key=len)

for x in arr:
    print(x)
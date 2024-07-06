n = int(input())

count_Not = 0
numbers = map(int, input().split())

for number in numbers:
    if number == 1:
        count_Not += 1
    for i in range(2, number):
        if number % i == 0:
            count_Not += 1
            break
print(n - count_Not)
num_list = []

for i in range(9):
    num = int(input())
    if num <= 100 and num not in num_list:
        num_list.append(num)

max = max(num_list)
print(max)
print( num_list.index(max) + 1)
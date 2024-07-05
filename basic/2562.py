Num_list = []

for i in range(9):
    Num = int(input())
    if Num <= 100 and Num not in Num_list:
        Num_list.append(Num)

Max = max(Num_list)
print(Max)
print( Num_list.index(Max) + 1)
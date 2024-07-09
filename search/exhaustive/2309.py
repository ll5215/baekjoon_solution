# dwarfs = []
# for i in range(9):
#     dwarfs.append(int(input()))

# found = False
# for i in range(9):
#     if found:
#         break
#     for j in range(i + 1, 9):
#         if found:
#             break
#         for k in range(j + 1, 9):
#             if found:
#                 break
#             for l in range(k + 1, 9):
#                 if found:
#                     break
#                 for m in range(l + 1, 9):
#                     if found:
#                         break
#                     for n in range(m + 1, 9):
#                         if found:
#                             break
#                         for o in range(n + 1, 9):
#                             if dwarfs[i] + dwarfs[j] + dwarfs[k] + dwarfs[l] + dwarfs[m] + dwarfs[n] + dwarfs[o] == 100:
#                                 result = [dwarfs[i], dwarfs[j], dwarfs[k], dwarfs[l], dwarfs[m], dwarfs[n], dwarfs[o]]
#                                 found = True
#                                 break

# result.sort()

# for dwarf in result:
#     print(dwarf)
    
    
# from itertools import combinations
    
# dwarfs = []
# for i in range(9):
#     dwarfs.append(int(input()))

# found = False
# for combination in combinations(dwarfs, 7):
#     if sum(combination) == 100:
#         result = sorted(combination)
#         found = True
#         break
# if found:
#     for dwarf in result:
#         print(dwarf)


dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))


total_height = sum(dwarfs)
excess_height = total_height - 100


found = False
dwarf1, dwarf2 = 0, 0
for i in range(9):
    for j in range(i + 1, 9):
        if dwarfs[i] + dwarfs[j] == excess_height:
            dwarf1 = dwarfs[i]
            dwarf2 = dwarfs[j]
            found = True
            break
    if found:
        break


dwarfs.remove(dwarf1)
dwarfs.remove(dwarf2)


dwarfs.sort()


for dwarf in dwarfs:
    print(dwarf)
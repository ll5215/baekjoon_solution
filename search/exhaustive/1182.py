# from itertools import combinations


# t, s = map(int, input().split())
# list = list(map(int, input().split()))
# count = 0

# for i in range(1, t+1):
#     comb = combinations(list, i)
    
#     for j in comb:
#         if sum(j) == s:
#             count += 1

# print(count)

def count_subsets(index, current_sum):
    global count
    if index == t:
        if current_sum == s:
            count += 1
        return
    # 현재 요소를 포함하지 않는 경우
    count_subsets(index + 1, current_sum)
    # 현재 요소를 포함하는 경우
    count_subsets(index + 1, current_sum + num_list[index])

t, s = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0

count_subsets(0, 0)

# 합이 0인 경우를 제외하기 위해 전체가 빈 경우의 수를 뺌
if s == 0:
    count -= 1

print(count)

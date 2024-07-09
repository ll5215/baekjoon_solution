import sys

t = int(sys.stdin.readline())
numbers = []

for i in range(t):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for num in numbers:
    print(num)

# 퀵 정렬 (메모리초과)
# import sys
# sys.setrecursionlimit(10**3)

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     left = []
#     right = []
#     pivot = arr[len(arr)//2]
    
#     for x in arr:
#         if x < pivot:
#             left.append(x)
#         else:
#             right.append(x)
#     right.remove(pivot)
#     return quick_sort(left) + [pivot] + quick_sort(right)
    
# t = int(sys.stdin.readline())
# numbers = []

# for i in range(t):
#     numbers.append(int(sys.stdin.readline()))
    
# sorted_numbers = quick_sort(numbers)

# for num in sorted_numbers:
#     print(num)
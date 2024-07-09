t = int(input())

height = list(map(int, input().split()))

stack = []

result = [0] * t

for i in range(t):
    while stack:
        if height[stack[-1]] < height[i]:
         stack.pop()
        else:
         result[i] = stack[-1] + 1
         break
    stack.append(i)

for i in range(t):
    print(result[i])
    

#오답 코드

# t = int(input())

# height = list(map(int, input().split()))

# stack = []

# result = [0] * t

# for i in range(t):
#     while stack:
#         if height[stack[-1]] < height[i]:
#          stack.pop()
#         else:
#          result[i] = stack[-1] + 1
#          break
#     stack.append(i)

   
# print(result)
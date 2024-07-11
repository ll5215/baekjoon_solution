def quad_tree(x, y, size):
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                half_size = size // 2
                return (
                    f"({quad_tree(x, y, half_size)}"
                    f"{quad_tree(x, y + half_size, half_size)}"
                    f"{quad_tree(x + half_size, y, half_size)}"
                    f"{quad_tree(x + half_size, y + half_size, half_size)})"
                )
    return color

n = int(input())
paper = [input().strip() for _ in range(n)]

result = quad_tree(0, 0, n)
print(result)




# import sys

# def quad_tree(x, y, size):
#     color = paper[x][y]  # 현재 영역의 첫 번째 색상
#     all_same = True  # 현재 영역이 모두 같은 색인지 확인하는 플래그

#     # 현재 영역의 모든 칸을 검사하여 같은 색인지 확인
#     for i in range(x, x + size):
#         for j in range(y, y + size):
#             if paper[i][j] != color:  # 다른 색이 발견되면
#                 all_same = False  # 같은 색이 아님을 표시
#                 break  # 내부 루프 중지
#         if not all_same:  # 같은 색이 아님이 확인되면
#             break  # 외부 루프 중지

#     if all_same:  # 영역이 모두 같은 색인 경우
#         return color  # 해당 색상 반환
#     else:  # 영역이 다른 색이 섞여 있는 경우
#         half_size = size // 2  # 영역을 네 부분으로 나눌 크기 계산
#         # 네 부분을 재귀적으로 호출하고 결과를 결합
#         top_left = quad_tree(x, y, half_size)
#         top_right = quad_tree(x, y + half_size, half_size)
#         bottom_left = quad_tree(x + half_size, y, half_size)
#         bottom_right = quad_tree(x + half_size, y + half_size, half_size)
#         return f"({top_left}{top_right}{bottom_left}{bottom_right})"

# input = sys.stdin.read
# data = input().split()
    
# n = int(data[0])  # 색종이의 크기 입력 받기
# paper = [data[i+1] for i in range(n)]  # 색종이의 색상 입력 받기

# result = quad_tree(0, 0, n)  # 전체 색종이에 대해 함수 호출
# print(result)  # 결과 출력



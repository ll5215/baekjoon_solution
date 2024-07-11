import sys

def count_colors(x, y, size):
    global white, blue
    initial_color = paper[x][y]  # 현재 영역의 첫 번째 색상
    same_color = True  # 현재 영역이 모두 같은 색인지 확인하는 플래그

    # 현재 영역의 모든 칸을 검사하여 같은 색인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != initial_color:  # 다른 색이 발견되면
                same_color = False  # 같은 색이 아님을 표시
                break  # 내부 루프 중지
        if not same_color:  # 같은 색이 아님이 확인되면
            break  # 외부 루프 중지

    if same_color:  # 영역이 모두 같은 색인 경우
        if initial_color == 0:  # 흰색일 경우
            white += 1  # 흰색 카운트 증가
        else:  # 파란색일 경우
            blue += 1  # 파란색 카운트 증가
    else:  # 영역이 다른 색이 섞여 있는 경우
        half_size = size // 2  # 영역을 네 부분으로 나눌 크기 계산
        count_colors(x, y, half_size)  # 1사분면
        count_colors(x, y + half_size, half_size)  # 2사분면
        count_colors(x + half_size, y, half_size)  # 3사분면
        count_colors(x + half_size, y + half_size, half_size)  # 4사분면

if __name__ == '__main__':
    n = int(sys.stdin.readline())  # 색종이의 크기 입력 받기
    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 색종이의 색상 입력 받기

    white, blue = 0, 0  # 흰색과 파란색 카운트 초기화
    count_colors(0, 0, n)  # 전체 색종이에 대해 함수 호출
    print(white)  # 흰색 색종이 조각 개수 출력
    print(blue)  # 파란색 색종이 조각 개수 출력

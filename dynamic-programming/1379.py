import heapq
import sys
input = sys.stdin.readline

def min_classrooms(lectures):
    # 강의들을 시작 시간 기준으로 정렬합니다.
    lectures.sort(key=lambda x: x[1])
    
    # 최소 힙 초기화
    heap = []
    
    # 첫 강의의 끝나는 시간을 힙에 추가합니다.
    heapq.heappush(heap, lectures[0][2])
    
    # 강의들을 순차적으로 처리합니다.
    for i in range(1, len(lectures)):
        # 힙의 최솟값(가장 빨리 끝나는 시간)을 확인하여 새로운 강의실이 필요한지 결정합니다.
        if heap[0] <= lectures[i][1]:
            heapq.heappop(heap)  # 현재 강의를 기존 강의실에 배정
        heapq.heappush(heap, lectures[i][2])  # 새로운 끝나는 시간 추가
    
    return len(heap)

# 입력 처리
n = int(input().strip())
lectures = []
for _ in range(n):
    number, start, end = map(int, input().strip().split())
    lectures.append((number, start, end))

# 결과 출력
print(min_classrooms(lectures))

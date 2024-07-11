n = int(input())
num = n
count = 0  

while True:
    digit_1 = num // 10  # 앞자리 수 구하기
    digit_2 = num % 10  # 뒷자리 수 구하기
    new_num = digit_1 + digit_2  # 새로운 수로 합치기
    new_num_digit_2 = new_num % 10  # 새로운 수의 뒷자리 수 구하기
    num = digit_2 * 10 + new_num_digit_2   # 원래 수의 뒷자리 수 + 새로운 수의 뒷자리 수 (*10은 2자리수로 만들기 위함)
    
    count = count + 1  # 실행되는 횟수 세기
    if num == n:  # 만약 num이 입력한 숫자와 같아지면 반복문 탈출
        break
    
print(count)  # 횟수 출력
a = int(input()) # 입력값
n = [] # 배열 선언
for i in range(1, a+1) : # 1 부터 a까지 값넣어
    if i % 3 != 0 : # 3의 배수가 아니라면
        n.append(i) # 배열에 i 값추가
print(*n)

n = int(input())
a = input().split()
d = []
for i in range(n) : # 0부터 n-1까지
    a[i] = int(a[i]) # 배열에 i 값추가 # a에 순서대로 저장
for i in range(n-1, -1, -1) : # 시작값은 입력값 -1 부터 -1 까지 -1 씩 감소한 값
    # n-1, n-2, ..., 3, 2, 1, 0
    print(a[i], end= ' ')

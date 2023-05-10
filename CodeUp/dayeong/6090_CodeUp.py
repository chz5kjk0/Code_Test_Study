a, m, d, n = map(int, input().split()) # 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 수 인지를 의미하는 정수(n)
for i in range(1, n) : # 1부터 n번째나오는 수까지 값 넣기
   a = a * m + d
print(a)

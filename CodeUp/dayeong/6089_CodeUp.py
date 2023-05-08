a, r, n = map(int, input().split()) # 시작 값(a), 등비의 값(r), 몇 번째 수 인지를 의미하는 정수(n)
for i in range(1, n) : # 1부터 n번째나오는 수까지 값 넣기
   a *= r
print(a)

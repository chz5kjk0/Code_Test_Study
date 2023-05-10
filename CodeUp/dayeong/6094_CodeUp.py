n = int(input()) # 무작위 출석 번호
a = list(map(int, input().split())) # 출석번호 리스트 저장
a.sort() # 오름차순 정렬
print(a[0]) # 가장 작은 값 출력

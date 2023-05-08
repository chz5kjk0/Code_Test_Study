n = int(input())
a = input().split()
d = []
for i in range(n) : # 0부터 n-1까지
    a[i] = int(a[i]) # 배열에 i 값추가 # a에 순서대로 저장
while d > a[i] :
    d = a[i]
print(d)   

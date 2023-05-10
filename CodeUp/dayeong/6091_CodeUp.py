a, b, c = map(int, input().split())
day = 1
while day % a != 0 or day % b != 0 or day % c != 0 : # day를 a,b,c 각자 나눠서 값이 같다면 0 일 것이다.
    # a,b,c 모두 day가 같아야 할 때 값을 구해야 하기 때문에 or을 사용
    day += 1 #day를 한개씩 늘려서 날마다 비교
print(day)

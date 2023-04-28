n = int(input())
for i in range(1, n+1) :
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9 : # 3으로 나눠서 나머지가 0인 경우는 왜 틀릴까요?
        print("X", end=' ')
    else :
        print(i, end = ' ')

﻿#6065
'''
@문제
3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

@입력
3개의 정수(a, b, c)가 공백을 두고 입력된다.
0 ~ +2147483647 범위의 정수들이 입력되며 적어도 1개는 짝수이다.

@출력
짝수만 순서대로 줄을 바꿔 출력한다.


'''

list_num = list(map(int, input().split()))

for i in list_num:
  if i%2==0:
    print(i)

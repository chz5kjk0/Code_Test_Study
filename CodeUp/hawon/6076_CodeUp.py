﻿'''
6076번
https://codeup.kr/problem.php?id=6076

@문제
정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

@입력
정수 1개가 입력된다.
(1 ~ 100)

@출력
0부터 그 수까지 줄을 바꿔 한 개씩 출력한다.
'''

endNum = int(input())


for i in range(0,endNum+1):
  print(i)

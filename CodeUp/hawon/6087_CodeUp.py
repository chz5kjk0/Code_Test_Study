﻿'''
6087 3의 배수는 통과 

@문제
1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
3의 배수인 경우는 출력하지 않도록 만들어보자.

예를 들면,
1 2 4 5 7 8 10 11 13 14 ...
와 같이 출력하는 것이다.


@입력
정수 1개를 입력받는다.
(1 ~ 100)


@출력
1부터 입력한 정수보다 작거나 같을 때까지 1씩 증가시켜 출력하되
3의 배수는 출력하지 않는다.


'''
num = int(input())

for i in range(1,num+1):
  if i%3==0:
    continue
  print(i, end=" ");

﻿'''
6089   수 나열하기2

@문제
시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때
n번째 수를 출력하는 프로그램을 만들어보자.


@입력
시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)가
공백을 두고 입력된다.(모두 0 ~ 10)

@출력
n번째 수를 출력한다.

'''
#시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)
a,r,n = map(int,input().split())

'''
a ar arr arrr ...
'''
print(a*(r ** (n-1)) )




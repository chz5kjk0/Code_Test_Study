﻿#6038

'''
@문제
정수 2개(a, b)를 입력받아
a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.

@입력
2개의 정수(a, b)가 공백으로 구분되어 입력된다.

@출력
a를 b번 거듭제곱한 값을 출력한다.

'''
a,b = map(int,input().split())
print(a**b)
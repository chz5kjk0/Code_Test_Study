﻿#6053

'''
@문제
정수값이 입력될 때,
그 불 값을 반대로 출력하는 프로그램을 작성해보자.

@입력
정수 1개가 입력된다.

@출력
입력된 정수의 불 값이 False 이면 True, True 이면 False 를 출력한다.

'''

a = bool(int(input()))#int로 입력받아서 T/F판단해서 변수에 저장
print(not a) 

﻿#6029번
'''
@문제설명
16진수를 입력받아 8진수(octal)로 출력해보자.

@입력
16진 정수 1개가 입력된다.

@출력
8진수 형태로 출력한다.


'''
n = int(input(),16) #입력받은 값을 16진수로 저장
print('%o'% n) # n을 8진수로 출력
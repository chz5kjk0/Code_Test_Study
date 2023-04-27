#6056
'''
@문제
2개의 정수값이 입력될 때,
그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.

@입력
2개의 정수가 공백을 두고 입력된다.

@출력
두 값의 True / False 값이 서로 다를 경우만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

'''
#XOR(exclusive or, 배타적 논리합) :참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산 
a, b = map(int, input().split())
print(bool(a) ^ bool(b)) # 비트를 XOR 연산하는 연산자 ^

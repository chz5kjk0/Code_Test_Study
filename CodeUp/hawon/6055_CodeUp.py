#6055
'''
@문제
2개의 정수값이 입력될 때,
그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

@입력
2개의 정수가 공백을 두고 입력된다.

@출력
하나라도 참일 경우 True 를 출력하고, 그 외의 경우에는 False 를 출력한다

'''

a, b = map(int, input().split())
print(bool(a) or bool(b))
# 자바의 ||연산자 파이썬에서는 안됨 print(bool(a) || bool(b))


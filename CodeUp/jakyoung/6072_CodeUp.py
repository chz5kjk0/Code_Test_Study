"""

6072 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1(설명)(py)

Q. 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

while 조건식 :
  ...
  ...
반복 실행구조를 사용해 보자.

0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

@ 입력
정수 1개가 입력된다.
(1 ~ 100)

@ 출력
1만큼씩 줄이면서 한 줄에 1개씩 카운트다운 수를 출력한다.

"""

'''
예시
...
while n!=0 :
  print(n)
  n = n-1
...

참고
n = n-1  #n에 저장되어있던 값에서 1만큼 뺀 후, 그 값을 다시 n에 저장시킨다.
n -= 1 과 같이 짧게 작성할 수도 있다. n -= 1 은 n = n-1 과 같은 의미이다.
이렇게 산술연산자(+, -, *, / ... )와 대입 연산자(=)를 함께 쓰는 것을 복합대입연산자라고도 부른다.
같은 방법으로 +=, *=, /=, //=, %=, &=, |=, ^=, >>=, <<=, **= 등과 같이 짧게 작성할 수 있다.

처음에 조건식을 검사하고, 그 다음에 실행하고, 그 다음에 값을 바꾸고...
다시 조건식을 검사하고, 실행하고, 값을 바꾸고...

'''

n = int(input())
while n != 0 :
  print(n)
  n -= 1 # n = n - 1

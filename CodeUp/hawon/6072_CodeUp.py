'''
6072번
https://codeup.kr/problem.php?id=6072

@문제
정수 1개 입력받아 카운트다운 출력하기1

@입력
정수 1개가 입력된다.
(1 ~ 100)

@출력
1만큼씩 줄이면서 한 줄에 1개씩 카운트다운 수를 출력한다.
'''
num = int(input())
while num != 0:
  print(num) #num을 출력한다
  num -= 1  #1을 뺸다


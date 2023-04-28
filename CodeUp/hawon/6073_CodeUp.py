'''
6073번
https://codeup.kr/problem.php?id=6073

@문제
정수 1개 입력받아 카운트다운 출력하기

@입력
정수 1개가 입력된다.
(1 ~ 100)

@출력
1만큼씩 줄이면서 카운트다운 수가 0이 될 때까지 한 줄에 1개씩 출력한다.
'''
num = int(input())

while num >= 0:
  num = num - 1 if num != 0 else num
  print(num)  #num을 출력한다
  if num == 0:
    break


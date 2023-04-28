'''
6078번
https://codeup.kr/problem.php?id=6078

@문제
영문 소문자 'q'가 입력될 때까지
입력한 문자를 계속 출력하는 프로그램을 작성해보자.


@입력
문자들이 1개씩 계속해서 입력된다.

@출력
영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력한다.
'''


while(True):
  a = input()
  print(a)
  if a == 'q':
    break


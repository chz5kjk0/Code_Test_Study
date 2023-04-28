'''
6074번
https://codeup.kr/problem.php?id=6074

@문제
영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

@입력
정수 1개가 입력된다.
(1 ~ 100)

@출력
a부터 입력한 문자까지 순서대로 공백을 두고 한 줄로 출력한다.
'''

end_cha = ord(input())
start = ord('a') #시작문자자

while start <= end_cha:
  print(chr(start), end=' ')  # 유니코드 문자: chr(정수값)
  start += 1


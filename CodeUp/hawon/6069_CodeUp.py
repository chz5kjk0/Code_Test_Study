#6069
'''
https://codeup.kr/problem.php?id=6069
@문제
평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?

@입력
영문자 1개가 입력된다.
(A, B, C, D 등 문자 1개가 입력된다.)

@출력
문자에 따라 다른 내용이 출력된다.


'''

s = input()

if s == 'A':
  print("best!!!")
elif s == 'B' :
  print("good!!")
elif s == 'C' :
  print("run!")
elif s == 'D' :
   print("slowly~")
else:
  print("what?")

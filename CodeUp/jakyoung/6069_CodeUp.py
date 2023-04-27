"""

6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기(py)

Q. 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?

@ 입력
영문자 1개가 입력된다.
(A, B, C, D 등 문자 1개가 입력된다.)

@ 출력
문자에 따라 다른 내용이 출력된다.

"""

'''


'''

'''
s = input()

if s == "A" :
  print("best!!!")

elif s == "B" :
  print("good!!")

elif s == "C" :
  print("run!")

elif s == "D" :
  print("slowly~")
  
else :
  print("what?")

'''

# 유니코드 활용
s = ord(input())

if s == 65 :
  print("best!!!")

elif s == 66 :
  print("good!!")

elif s == 67 :
  print("run!")

elif s == 68 :
  print("slowly~")
  
else :
  print("what?")
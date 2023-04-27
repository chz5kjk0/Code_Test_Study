"""

6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)

Q. 월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
 12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
9, 10, 11 : fall

@ 입력
월을 의미하는 1개의 정수가 입력된다.(1 ~ 12)

@ 출력
계절 이름을 출력한다.

"""

'''
예시
...
if n//3==1 :
  print("spring")
...

참고
때때로 수들의 특징을 관찰하고 이용하면 매우 간단히 해결할 수도 있다.

'''

'''
m = int(input())

if m <= 2 or m == 12 :
  print("winter")

elif m >= 3 and m <= 5 :
  print("spring")

elif m >= 6 and m <= 8 :
  print("summer")

elif m >= 9 and m <= 11 :
  print("fall")
  
else :
  print("what?")
'''

# 다른 풀이
m = int(input())

if m // 3 == 0 or m == 12 :
  print("winter")

elif m // 3 == 1 :
  print("spring")

elif m // 3 == 2 :
  print("summer")

elif m // 3 == 3 :
  print("fall")
  
else :
  print("what?")
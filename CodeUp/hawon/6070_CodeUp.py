#6070
'''
https://codeup.kr/problem.php?id=6070
@문제
월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall

@입력
월을 의미하는 1개의 정수가 입력된다.(1 ~ 12)

@출력
계절 이름을 출력한다.


'''

m = int(input())

if m//3 == 1 :
  print("spring")
elif m//3 == 2 :
  print("summer")
elif m//3 == 3 :
  print("fall")
else:
  print("winter")

'''
[출력] 문자열 반복해서 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/181950
'''

a, b = input().strip().split(' ')
b = int(b)

for i in range (b): # 0부터 b-1 까지 반복
    print(a, end='') # 줄바꿈없이 반복하여 출력

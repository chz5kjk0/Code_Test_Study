'''
[출력, 연산] 홀짝 구분하기
https://school.programmers.co.kr/learn/courses/30/lessons/181944
'''

a = int(input())

if a % 2 == 0 : # a가 짝수일 경우 (2로 나눈 나머지가 0)
    print(a, 'is even')
else : # a가 홀수일 경우 (2로 나눈 나머지가 0이 아닐 경우)
    print(a, 'is odd')

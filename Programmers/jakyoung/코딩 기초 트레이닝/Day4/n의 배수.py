'''
[연산, 조건문] n의 배수
https://school.programmers.co.kr/learn/courses/30/lessons/181937
'''

def solution(num, n):
    answer = 0
    
    if num % n == 0 :
        answer = 1
    
    return answer

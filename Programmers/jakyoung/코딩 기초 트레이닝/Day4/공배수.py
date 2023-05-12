'''
[연산, 조건문] 공배수
https://school.programmers.co.kr/learn/courses/30/lessons/181936
'''

def solution(number, n, m):
    answer = 0
    
    if number % n == 0 and number % m == 0 :
        answer = 1
    
    return answer

'''
[조건문, 반복문] 수 조작하기 1
https://school.programmers.co.kr/learn/courses/30/lessons/181926
'''

def solution(n, control):
    answer = 0
    
    for letter in control :
        if letter == 'w' :
            n += 1
        if letter == 's' :
            n -= 1
        if letter == 'd' :
            n += 10
        if letter == 'a' :
            n -= 10
    
    answer = n
    
    return answer

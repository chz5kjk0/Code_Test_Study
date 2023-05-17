'''
[조건문] 주사위 게임 2
https://school.programmers.co.kr/learn/courses/30/lessons/181930
'''

def solution(a, b, c):
    answer = 0
    
    if a == b and b == c : # a, b, c 세 수가 모두 같은 경우
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a != b and b != c and a != c : # a, b, c 세 수가 모두 다른 경우
        answer = a + b + c
    else : # 그 외의 경우 (세 수 중에 두 수만 같은 경우)
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    
    return answer

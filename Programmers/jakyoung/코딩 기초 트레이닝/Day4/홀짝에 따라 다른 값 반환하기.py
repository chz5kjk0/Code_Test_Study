'''
[연산, 조건문] 홀짝에 따라 다른 값 반환하기
https://school.programmers.co.kr/learn/courses/30/lessons/181935
'''

def solution(n):
    answer = 0
    
    if n % 2 == 1 :
        for i in range (1, n+1, 2) : # start, end, step
            answer += i
            if i > n :
                break
    else :
        for i in range (0, n+1, 2) :
            answer += i**2
            if i > n :
                break
    
    return answer

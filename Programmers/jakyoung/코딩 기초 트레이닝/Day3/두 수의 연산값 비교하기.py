'''
[연산] 두 수의 연산값 비교하기
https://school.programmers.co.kr/learn/courses/30/lessons/181938
'''

def solution(a, b):
    answer = 0
    
    if int(str(a) + str(b)) >= 2 * a * b :
        answer = int(str(a) + str(b))
    else :
        answer = 2 * a * b
    
    return answer

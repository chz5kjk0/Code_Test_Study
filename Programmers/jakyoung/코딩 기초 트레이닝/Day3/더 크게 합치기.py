'''
[연산] 더 크게 합치기
https://school.programmers.co.kr/learn/courses/30/lessons/181939
'''

def solution(a, b):
    answer = 0
    
    if int(str(a) + str(b)) >= int(str(b) + str(a)) :
        answer = int(str(a) + str(b))
    else :
        answer = int(str(b) + str(a))
    
    return answer

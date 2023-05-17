'''
[조건문] 원소들의 곱과 합
https://school.programmers.co.kr/learn/courses/30/lessons/181929
'''

def solution(num_list):
    answer = 0
    mul = 1 # 곱 변수
    sum = 0 # 합 변수
    
    for i in range (len(num_list)) :
        mul *= num_list[i]
        sum += num_list[i]
    
    if mul < sum**2 :
        answer = 1
    
    return answer

'''
[조건문, 반복문] 마지막 두 원소
https://school.programmers.co.kr/learn/courses/30/lessons/181927
'''

def solution(num_list):
    answer = num_list
    
    last = len(num_list) - 1
    
    if num_list[last] > num_list[last - 1] :
        num_list.append(num_list[last] - num_list[last - 1])
    else :
        num_list.append(2 * num_list[last])
    
    return answer

'''
[조건문] 이어 붙인 수
https://school.programmers.co.kr/learn/courses/30/lessons/181928
'''

def solution(num_list):
    answer = 0
    
    odd = '' # 홀수
    even = '' # 짝수
    
    for i in range (len(num_list)) :
        if num_list[i] % 2 == 0 :
            even += str(num_list[i]) # 문자열로 형변환
        else :
            odd += str(num_list[i])
    
    answer = int(even) + int(odd) # 정수로 형변환
    
    return answer

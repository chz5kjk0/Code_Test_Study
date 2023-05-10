'''
[출력, 연산] 문자열 겹쳐쓰기
https://school.programmers.co.kr/learn/courses/30/lessons/181943
'''

def solution(my_string, overwrite_string, s):
    answer = ''
    
    answer += my_string[:s] # 문자열 my_string 을 s(시작점) 전까지 결합
    answer += overwrite_string # 문자열 overwrite_string 결합
    answer += my_string[s+len(overwrite_string):] # 문자열 my_string 에서 overwrite_string 이후의 문자열 결합
    
    return answer

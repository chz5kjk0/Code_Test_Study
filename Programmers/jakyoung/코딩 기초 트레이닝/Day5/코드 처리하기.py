'''
[조건문] 코드 처리하기
https://school.programmers.co.kr/learn/courses/30/lessons/181932
'''

def solution(code):
    ret = ''
    mode = 0
    code = list(code)
    
    for idx in range (len(code)) :
        if mode == 0 :
            if code[idx] != '1' and idx % 2 == 0 :
                ret += code[idx]
            if code[idx] == '1' :
                mode = 1
                continue
    
        if mode == 1 :
            if code[idx] != '1' and idx % 2 == 1 :
                ret += code[idx]
            if code[idx] == '1' :
                mode = 0
                continue
                
    if ret == '' :
        ret = 'EMPTY'
    
    return ret

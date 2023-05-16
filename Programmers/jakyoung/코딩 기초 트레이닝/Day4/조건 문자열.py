'''
[연산, 조건문] 조건 문자열
https://school.programmers.co.kr/learn/courses/30/lessons/181934
'''

def solution(ineq, eq, n, m):
    answer = 0
    '''
    Python 3.10에 도입된 Match case 활용
    match (ineq, eq)
        case (">", "=") :
            if n >= m :
                answer = 1
        
        case ("<", "=") :
            if n <= m :
                answer = 1
        
        case (">", "!") :
            if n > m :
                answer = 1
            
        case ("<", "!") :
            if n < m :
                answer = 1
    '''
    
    if ineq == ">" and eq == "=" and n >= m :
        answer = 1
    elif ineq == "<" and eq == "=" and n <= m :
        answer = 1
    elif ineq == ">" and eq == "!" and n > m :
        answer = 1
    elif ineq == "<" and eq == "!" and n < m :
        answer = 1
    
    return answer

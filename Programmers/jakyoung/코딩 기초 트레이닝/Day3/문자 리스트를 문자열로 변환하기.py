'''
[연산] 문자 리스트를 문자열로 변환하기
https://school.programmers.co.kr/learn/courses/30/lessons/181941
'''

def solution(arr):
    answer = ''
    
    for i in range (len(arr)) :
        answer += arr[i]
    
    return answer

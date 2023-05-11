'''
[연산] 문자열 섞기
https://school.programmers.co.kr/learn/courses/30/lessons/181942
'''

def solution(str1, str2):
    answer = ''
    
    '''
    # list1 = list(str1)
    # list2 = list(str2)
    # 'int' object is not iterable 오류
    
    list1 = []
    list2 = []
    
    for i in str1 :
        list1.append(i)
    for j in str2 :
        list2.append(j)
    
    for i in len(list1) :
        answer += list1[i]
        answer += list2[i]
    '''
    
    '''
    zip() :
    - 여러 개의 iterable 자료형(리스트, 튜플과 같이 반복 가능한 자료형)이 개수가 동일할 때 사용 
    - iterable 자료형의 각각의 요소를 나눈 후 순서대로 묶어서 요소 개수만큼 새로운 iterable 자료형을 생성
    
    '''
    
    for s1, s2 in zip(str1, str2) :
        answer += s1
        answer += s2
    
    return answer

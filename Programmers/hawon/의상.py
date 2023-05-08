'''
https://school.programmers.co.kr/learn/courses/30/lessons/42578
'''

def solution(clothes):
    
    #딕셔너리 생성
    clotheType =  {}
    
    for i,j in clothes:
        #옷의 종류를 key로 잡고 종류별 옷 개수 카운트
        clotheType[j] = clotheType.get(j,0) + 1
        
    answer = 1
    #선택 가능한 조합 구하기: 종류별 갯수 곱, 안입는 경우를 고려하여 +1
    for k in clotheType:
        answer = answer*(clotheType[k]+1)
        
    #아무것도 안입었을 경우를 제외
    answer -= 1
    return answer

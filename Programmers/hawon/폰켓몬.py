'''
https://school.programmers.co.kr/learn/courses/30/lessons/1845
'''
def solution(nums):
    
    #고를 수 있는 총 포켓몬 수
    chooseNum = len(nums)/2
    
    #set객체로 중복을 제거한 포켓몬 수 len(set(nums))
    return len(set(nums)) if len(set(nums)) <  chooseNum else chooseNum

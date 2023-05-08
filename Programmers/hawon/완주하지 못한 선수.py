'''
https://school.programmers.co.kr/learn/courses/30/lessons/42576
'''

#마라톤에 참여한 선수들의 이름이 담긴 배열 participant
#완주한 선수들의 이름이 담긴 배열 completion
def solution(participant, completion):
    part_dict = {}
    sumHash = 0
    
    #마리톤에 참여한 선수이름의 해시값을 key로 잡고 value에 이름 넣어주기
    for p in participant:
        part_dict[hash(p)] =  p
        sumHash += hash(p)
    
    #완주한 선수의 이름 해시값 빼기
    for c in completion:
        sumHash -=  hash(c)
    
    return part_dict.get(sumHash)

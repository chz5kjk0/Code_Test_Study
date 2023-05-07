def solution(nums):
    answer = 0
    
    # 중복 제거한 배열의 길이 (폰켓몬 종류의 수)
    monNum = len(set(nums))
    # 선택되는 폰켓몬의 수
    selectNum = len(nums) // 2
    
    if selectNum <= monNum : # 선택되는 폰켓몬의 수가 폰켓몬 종류의 수보다 작거나 같은 경우
        answer = selectNum # 최대 고를 수 있는 폰켓몬 종류의 수 = 선택되는 폰켓몬의 수
    
    else : # 선택되는 폰켓몬의 수가 폰켓몬 종류의 수보다 큰 경우
        answer = monNum # 최대 고를 수 있는 폰켓몬 종류의 수 = 폰켓몬 종류의 수
    
    return answer

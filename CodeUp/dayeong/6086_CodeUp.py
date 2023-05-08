a = int(input()) # 입력값
sum = 0 # 합계
n = 0 # 1씩더하는 값
while sum < a : # 합계가 입력한 값보다 작을때
    n = n + 1   # 1, 2, 3 ... 순서대로 더해서 합함
    sum = sum + n
   
print(sum) 

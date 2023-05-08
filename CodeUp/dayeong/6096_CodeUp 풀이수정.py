# 바둑판 생성 20 * 20
arr = []
for i in range(20) :
    arr.append([]) # arr = ([], [], ... [20])
    for j in range(20) :
        arr[i].append(0) # arr = ([], [], ... [20], [],[] ... [20])

for i in range(19) :
    num = input().split()
    for j in range(19) :
        arr[int(i+1)][int(j+1)] = int(num[j]) 
# 입력값에 해당하는 값만큼 뒤집기
n = int(input())
for i in range(n) :
    x, y = map(int, input().split())
    for j in range(1, 20) :
        if arr[x][j] == 0 :
            arr[x][j] = 1
        else :
            arr[x][j] = 0
        if arr[j][y] == 0 :
            arr[j][y] = 1
        else :
            arr[j][y] = 0        

# 뒤집은 바둑판 출력
for i in range(1, 20) :
    for j in range(1, 20) :
      print(arr[i][j], end = ' ')
    print()

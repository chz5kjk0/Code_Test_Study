num = int(input())
# 바둑판 생성 20 * 20
arr = []
for i in range(20) :
    arr.append([]) # arr = ([], [], ... [20])
    for j in range(20) :
        arr[i].append(0) # arr = ([], [], ... [20], [],[] ... [20])

# 입력값에 해당하는 좌표값 1로 변경
for i in range(num) :
    x, y = map(int, input().split())
    arr[(x)][(y)] = 1

# 전체 출력
for i in range(1, 20) :
    for j in range(1, 20) :
      print(arr[i][j], end = ' ')
    print()
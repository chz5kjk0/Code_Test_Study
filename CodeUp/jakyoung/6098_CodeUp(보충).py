"""

6098 : [기초-리스트] 성실한 개미(py)

Q. 미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.

@ 입력
10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.

@ 출력
성실한 개미가 이동한 경로를 9로 표시해 출력한다.

"""

'''


'''

# 배열 생성
m = []

for i in range (10) : # 0 ~ 9
  m.append([])
  for j in range(10) :
    m[i].append(0)

# 배열에 값 입력
for i in range (10) :
  arr = []
  arr = input().split()
  
  for j in range (10) :
    arr[j] = int(arr[j])
    m[i][j] = arr[j]
    
# 배열의 값 바꾸기
x, y = 1, 1 # 출발점
arr[x][y] = 9
while True:
  # 오른쪽으로 갈 수 있는지
  if m[x][y+1] == 0 : # 오른쪽으로 이동 가능할 경우
    m[x][y+1] = 9
    y += 1
    continue

  # 아래쪽으로 갈 수 있는지
  if m[x+1][y] == 0 :
    m[x+1][y] == 9
    x += 1
    continue

  # 먹이를 찾은 경우
  if m[x][y+1] == 2 :
    m[x][y+1] = 9
    break

  if m[x+1][y] == 2 :
    m[x+1][y] = 9
    break

  # 더 이상 움직일 수 없는 경우
  if (m[x][y+1] == 1 and m[x+1][y] == 1) or (x == 9 and y == 9) : 
    break
    

for i in range (10) :
  for j in range (10) :
    print(m[i][j], end=' ')
  print()

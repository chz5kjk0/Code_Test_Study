"""

6097 : [기초-리스트] 설탕과자 뽑기(py)

Q. 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

@ 입력
첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
1 <= w, h <= 100
1 <= n <= 10
d = 0 or 1
1 <= x <= 100-h
1 <= y <= 100-w

@ 출력
모든 막대를 놓은 격자판의 상태를 출력한다.
막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
단, 각 숫자는 공백으로 구분하여 출력한다.

"""

'''


'''

# 격자판 입력
h, w = map(int, input().split())

# 격자판 생성, 0으로 초기화
m = []
# 0 ~ h, 0 ~ w 까지의 격자판을 만들고 (0, j), (i, 0) 은 공백으로 둠
for i in range(h+1) : 
  m.append([])
  for j in range(w+1) :
    m[i].append(0)

n = int(input())

for i in range (n) :
  l, d, x, y = map(int, input().split())
  
  if d == 0 : # 가로인 경우
    for j in range (l) : # 막대 길이만큼 y 값이 증가
      # m[x-1][y-1+j] = 1
      m[x][y+j] = 1

  else : # 세로인 경우
    for j in range (l) : # 막대 길이만큼 x 값이 증가
      # m[x-1+j][y-1] = 1
      m[x+j][y] = 1

# 출력
for i in range (1, h+1) :
  for j in range (1, w+1) :
    print(m[i][j], end=' ')
  print()

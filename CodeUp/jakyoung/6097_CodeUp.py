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

h, w = map(int, input().split())
n = int(input())

m = []

for i in range(h+1) :
  m.append([])
  for j in range(w+1) :
    m[i].append(0)

for i in range (n) :
  l, d, x, y = map(int, input().split())
  if d == 0 :
    for j in range (l) :
      # m[x-1][y-1+j] = 1
      m[x][y+j] = 1

  else :
    for j in range (l) :
      # m[x-1+j][y-1] = 1
      m[x+j][y] = 1

for i in range (1, h+1) :
  for j in range (1, w+1) :
    print(m[i][j], end=' ')
  print()
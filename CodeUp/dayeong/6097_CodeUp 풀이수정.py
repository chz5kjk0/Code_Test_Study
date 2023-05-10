h, w = map(int, input().split())

# h, w 크기 만큼의 격자판 생성
arr = []
for i in range(h+1) :
  arr.append([])
  for j in range(w+1) :
    arr[i].append(0)

n = int(input()) # 막대 개수
for i in range(n) :
  l,d,x,y = map(int, input().split()) #막대길이, 방향, 좌표 입력
  # ㅣ,d 값이 막대의 형태를 정해주고 x,y 좌표값에 표시
  if d == 0 : 
    for j in range(l) :
      arr[x][y+j] = 1
  else :
    for j in range(l) :
      arr[x+j][y] = 1
# 최종 값 출력      
for i in range(1, h+1) :
  for j in range(1, w+1) :
    print(arr[i][j], end = ' ')
  print()

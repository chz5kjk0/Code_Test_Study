﻿'''
6096 바둑알 십자 뒤집기

@문제
부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

"십(+)자 뒤집기를 해볼까?"하고 생각했다.

십자 뒤집기는
그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 
다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

@입력
바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
십자 뒤집기 횟수(n)가 입력된다.
십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.

@출력
십자 뒤집기 결과를 출력한다.
'''

#흰 돌의 개수(n)
table = [[0 for _ in range(19)] for _ in range(19)]

#바둑판 입력받기
for i in range(19):
  oneLine = list(map(int,input().split()))
  for j in range(19):
    table[i][j] = oneLine[j]

n = int(input())
#입력받은 십자 뒤집기 횟수만큼 뒤집기 실행
for k in range(n):
  #십자 뒤집기 좌표
  x,y = map(int, input().split())

  for j in range(19):
    table[x-1][j] = 0 if table[x-1][j] == 1 else 1
    table[j][y-1] = 0 if table[j][y-1] == 1 else 1

#바둑판 출력
for row in table:
  for stone in row:
    print(stone, end=' ')
  print()



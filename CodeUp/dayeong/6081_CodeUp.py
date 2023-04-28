n = input()
n = int(n, 16) # 16진수 입력방법 
for i in range(1, 16) :
    print('%X'%n, '*%X'%i, '=%X'%(n*i),sep='')

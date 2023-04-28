n = ord(input())

while n != ord('q') : # 아스키코드 입력값은 아스키코드로 형변환한 값과 비교해야함
    print(chr(n))
    n = ord(input())
    
print(chr(n))  

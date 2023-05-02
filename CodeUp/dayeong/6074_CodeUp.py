a = ord(input()) # 입력값
s = ord('a') # 시작값
while a >= s:
    print(chr(s) , end=' ') # 시작값(유니코드), end = ' ' 값 출력 후 공백문자 ' '를 출력한다. 생략시 줄바꿈됨
    s += 1

#6019번
'''
입력
연도, 월, 일이 닷('.')으로 구분되어 입력된다.

출력
대시(마이너스 기호)를 구분기호로 사용해서
일-월-연도로 바꿔 출력한다.

'''

year,month,day = input().split('.') 
print(day,month,year, sep='-')

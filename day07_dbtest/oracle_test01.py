import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','192.168.1.17:1521/XE')
cursor = conn.cursor()
cursor.execute("select * from emp")

for item in cursor:
    print(item[1],item[5])

conn.close()


while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요:
1. 사원 검색 2. 사원 찾기
>>>''').upper()
    if choice == "1":
        while True:
            print('job을 입력해주세요')
            input('job')

# pip install ex_Oracle
# 치킨 피자 탕수육 짜장면 짬뽕
# git 연습용 내용 추가
import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','192.168.1.17:1521/XE')
cursor = conn.cursor()
cursor.execute("select * from emp where deptno = 10")

for item in cursor:
    print(item[1],item[5])

conn.close()



import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','192.168.1.8:1521/XE')
cursor = conn.cursor()
cursor.execute("create table fruitlist (name varchar2(20), price number(10),cnt number(10))")

insert into fruitlist values (1, '사과', '2000', 10)
insert into fruitlist values (2, '포도', '3000', 20)
insert into fruitlist values (3, '수박', '10000', 5)



for row in items:
    sql = "insert into fruitlist items(:1,:2,:3)"
cursor.execute(sql)


sql = "update fruitlist set price=:1 where fruitlist_id=:2"
data=(6000,40)
cursor.execute(sql,data)
cursor.close()
conn.commit()
conn.close()

sql = "delete from fruitlist where fruitlist_id=3"
cursor.execute(sql)
cursor.close()
conn.commit()
conn.close()

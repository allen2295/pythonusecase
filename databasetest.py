#数据库测试
import mysql.connector
conn = mysql.connector.connect(user = 'root', password = 'password', host='127.0.0.1', database = 'test', auth_plugin='mysql_native_password')
cursor = conn.cursor()
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['3', 'Michael'])
cursor.rowcount
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('2',))
values = cursor.fetchall()
print(values)
#[('1', 'Michael')]
# 关闭Cursor和Connection:
cursor.close()
conn.close()
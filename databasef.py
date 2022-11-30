#数据库读写函数
import mysql.connector
def database_init():
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='test',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute('create table useraccount (id varchar(20) primary key, name varchar(20), password varchar(20))')
    #cursor.execute('insert into useraccount (id, name) values (%s, %s)', ['3', 'Michael'])
    #cursor.rowcount
    conn.commit()
    cursor.close()

def set_useraccount(userid, username, password):
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='test',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into useraccount (id, name, password) values (%s, %s, %s)', [userid, username, password])
    #cursor.rowcount
    conn.commit()
    cursor.close()

def get_useraccountByid():
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='test',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    #cursor.execute('select * from useraccount where id = %s', (x ,))
    cursor.execute('select * from useraccount', )
    values = cursor.fetchall()
    # [('1', 'Michael')]
    # 关闭Cursor和Connection:
    cursor.close()
    conn.close()
    return values



#db.py
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor)
            print("Connection Successful")
            return conn
    except pymysql.MySQLError as e:
        print(e)
        return("conn failed")
    return pymysql.connect(user=db_user, password=db_password,
                unix_socket=unix_socket, db=db_name,                    cursorclass=pymysql.cursors.DictCursor)


def auth_user(employee_id, password):
    conn = open_connection()
    with conn.cursor() as cursor: 
        result = cursor.execute('SELECT * FROM Employee WHERE employee_id = %s and password = %s', (employee_id, password))
        customers = cursor.fetchall()
        if result > 0:
            got_customers = "auth pass"
        else:
            got_customers = "Authentication Failed"
    conn.close()
    return got_customers

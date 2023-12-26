#!C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe
print("content-type:text/html\r\n\r\n")

import pymysql
import cgi
connection = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = connection.cursor()
f = cgi.FieldStorage()


a = """select * from gk where sno=1"""
cur.execute(a)
r = cur.fetchone()
print(r[6])
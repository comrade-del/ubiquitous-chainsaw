#!C:\Users\Me\AppData\Local\Programs\Python\Python310\python.exe
print("Content-Type: text/html\n")
print()
import cgi

form=cgi.FieldStorage()

name=form.getvalue('name')
age=form.getvalue('number')
gender=form.getvalue('gender')
grade=form.getvalue('grade')

import mysql.connector

conn = mysql.connector.connect(
        host = "localhost",
        database="test",
        user="root",
        password="allow",
        port=3306)

cursor = conn.cursor()

table1="announced_lga_results"
cursor.execute("SELECT * from %s where lga_name=%s"%(table1,age))
result1 = cursor.fetchall()

p = []

tbl = "<thead><tr><th>Result_id</th><th>Polling_Unit_Uniqueid</th><th>Party_Abbreviation</th><th>Party_Score</th></tr><\t"
p.append(tbl)

for row in result1:
    a = "<tr><td>%s</td>"%row[0]
    p.append(a)
    b = "<td>%s</td>"%row[1]
    p.append(b)
    c = "<td>%s</td>"%row[2]
    p.append(c)
    d = "<td>%s</td></tr>"%row[3]
    p.append(d)

contents1 = '''<!DOCTYPE html>
<html>
<head>
<title>All</title>
<h1>Results for all polling units</h1>
</head>
<body>
<a href="webbrowser2.html" target=_blank>Get total results by LG</a>
<table>
%s
</table>
</body>
</html>
'''%(p)

f = open("webbrow.html", "w")
f.write(contents1)
f.close()

cursor.execute("insert into student values (%s,%s,%s,%s)",(name, number, gender, age))
con.commit()

cur.close()
con.close()
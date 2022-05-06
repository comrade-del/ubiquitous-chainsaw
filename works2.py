import mysql.connector

conn = mysql.connector.connect(
        host = "localhost",
        database="test",
        user="root",
        password="allow",
        port=3306)

if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")
    
cursor = conn.cursor()
table="announced_pu_results"
table1="announced_lga_results"
cursor.execute("SELECT * from %s "%table)
result1 = cursor.fetchall()

p = [] #to save sql table values in list

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
    
num=int(input("lga id: "))
cursor.execute("SELECT * from %s where lga_name=%d"%(table1,num))
result2 = cursor.fetchall()
l=[] #same as list p, different table
tbl2 = "<thead><tr><th>Result_id</th><th>LGA_Name</th><th>Party_Abbreviation</th><th>Party_Score</th></tr><\t"

l.append(tbl2)

for row in result2:
    a = "<tr><td>%s</td>"%row[0]
    l.append(a)
    b = "<td>%s</td>"%row[1]
    l.append(b)
    c = "<td>%s</td>"%row[2]
    l.append(c)
    d = "<td>%s</td></tr>"%row[3]
    l.append(d)

cursor.execute("SELECT SUM(party_score) FROM %s where lga_name=%d;"%(table1,num)) #sum of select values in selected colulmn
tota = cursor.fetchall()
for i in tota:
    tot=i
cursor.execute("SELECT lga_name from %s ORDER BY lga_name"%(table1)) #tried to make drop-down numbers in ascending order, not complerely successful, just followed database order
result3 = cursor.fetchall()
s=[]
for row in result3:
    e = '<option value="%s">%s</option>'%(row[0],int(row[0]))
    s.append(e)

res = [] #remove repetitions in drop-down
for i in s:
    if i not in res:
        res.append(i)    

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
'''%(p) #first webpage, worked as intended 

contents2 = '''<!DOCTYPE html>
<html>
<head>
<title>Select Total</title>
</head>
<body>
<a href="webbrowser.html">All Polling units</a>
<form action="works2.ipynb" method="get">
<label for="lga">LGA id</label>
<select name="lga" id="lga">
%s
</select>
<input type="submit" value="Submit">
</section>
</form>
<table>
%s
<tfoot>
<td>Total</td>
<td>%s</td>
</tfoot>
</table>
</body>
</html>
'''%(res,l,tot) #second webpage, worked as expected when ran as python script on jupyter, submitting form returns code

f = open("webbrowser.html", "w")
f.write(contents1)
f.close()
d = open("webbrowser2.html", "w")
d.write(contents2)
d.close()


if(conn.is_connected()):
    cursor.close()
    conn.close()
    print("MySQL connection is closed.")  

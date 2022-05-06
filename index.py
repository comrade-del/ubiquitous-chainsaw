#!C:\Users\Me\AppData\Local\Programs\Python\Python310\python.exe
#practice not related to work
import cgi
form_inputs = cgi.FieldStorage()
print("Content-Type: text/html\n")

if form_inputs.getvalue('name') is None:
    input_name=''
else:
    input_name=form_inputs.getvalue('name')
    
input_gender = '' if form_inputs.getvalue('gender') is None else form_inputs.getvalue('gender')

input_grade = '' if form_inputs.getvalue('grade') is None else form_inputs.getvalue('grade')

print('<form action="?" method="post">')
print('<input type="text" placeholder="first name" id="name" value="'+ str(input_name) + '" name="name">')


print('<input type="number" placeholder="number" id="number" name="number">')

#input_number = 0 if form_inputs.getvalue('number') is 0 else form_inputs.getvalue('number')

print('&nbsp;&nbsp;')

print('<input type="radio" id="male" name="gender" value="male">Male')
print('<input type="radio" id="female" name="gender" value="female">Female')

print('&nbsp;&nbsp;')

selected_grade_a=''
if input_grade=='a':
    selected_grade_a='selected'

print('<select id="grade" name="grade">')
print('<option value="">Grade</option>')
print('<option value="a" '+ selected_grade_a+ '>A</option>')
print('<option value="b">B</option>')
print('<option value="c">C</option>')
print('<option value="d">D</option>')
print('<option value="e">E</option>')
print('<option value="f">F</option>')
print('</select>')

print('&nbsp&nbsp;')

print('<input type="submit" value="Send">')
print('</form>')

print(str(input_name),'<br>')
print(str(input_gender),'<br>')
print(str(input_grade),'<br>')
dig=int(form_inputs.getvalue('number'))
#c=dig+2
print('Your number + 2 = ',dig+2)

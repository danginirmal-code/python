import sqlite3
connection=sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute('''
Create table If Not Exists employees(
id Integer Primary Key,
name Text Not Null,
age Integer,
department text
)
''')
##Commit the changes
connection.commit()

# cursor.execute('''
# Insert into employees(name,age,department) values('nirmal',25,'Finance')
# ''')
connection.commit()

cursor.execute('update employees set age=34 where name="nirmal"')
connection.commit()
cursor.execute('select * from employees')
cursor.execute('''
delete from employees where name="nirmal"
''')
rows=cursor.fetchall()
for row  in rows:
    print(row)
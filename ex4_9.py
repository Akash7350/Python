import psycopg2
con=psycopg2.connect(database='mydatabase',user='postgres',password='',host='localhost',port=5432)
c1=con.cursor()
c1.execute('select * from course')
data=c1.fetchall()
sid=int(input('Enter the Student id : '))
sname=input('Enter the student name')
print('Select  course id from the follwing : ')
print(data)
cid=int(input('Enter the course id'))
row=(sid,sname,cid)
c1.execute('insert into student values(%s,%s,%s) ',row)


con.commit()
print('Record Inserted Successfully')
con.close()

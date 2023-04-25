import psycopg2
#create connection
con=psycopg2.connect(database='mydatabase',user='postgres',password='',host='localhost',port=5432)
#crete cursor
c1=con.cursor()
c1.execute('select count (*) from student')
data=c1.fetchall()
print('Number of student =', data)
con.close()

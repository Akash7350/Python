import psycopg2
#create 
con=psycopg2.connect(database='mydatabase',user='postgres',password='',host='localhost',port=5432)
#crete 
c1=con.cursor()
c1.execute('create table dept(dno int primary key, dname varchar (30) )')
c1.execute('create table emp(eno int primary key, ename varchar (30), did int references dept(dno))')
con.commit()
con.close()


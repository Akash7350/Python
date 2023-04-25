import psycopg2
#create connection
con=psycopg2.connect(database='mydatabase',user='postgres',password='',host='localhost',port=5432)
#crete cursor
c1=con.cursor()
c1.execute("select table_name from information_schema.tables where table_schema='public'")
data=c1.fetchall()
print('Tables name are')
for d in data:
	print(d)
con.close()

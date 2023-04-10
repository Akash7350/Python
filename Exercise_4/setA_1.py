class person:
	def __init__(self):
		self.pid=1
		self.pname='Akash'
		self.age=19
	def __init__(self,pid,pname,age):
		self.pid=pid
		self.pname=pname
		self.age=age
	
	def msg(self):
		print('Hello')
	def display2(self,msg):
		print (msg)
		
	def __str__(self):
		return 'pid={} \n pname=",self.pname\n name=self.pname\n age={self.age}'
			
	def display3(self):
		print('id=',self.pid, 'name',self.pname,'age=',self.age)


#Driver code reating object 
ob1=person()
ob1.msg()
ob2=person()
ob2.display2('Indira')
ob3=person()
ob3.display3()
ob4=person(2,'abhi',19)
ob4=display4() '''
ob5=person(5,'as',45)
print(ob5)

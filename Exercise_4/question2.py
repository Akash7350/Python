class circle:
	r=0
	pi=3.14
	def __init__(self,r,pi):
		self.r=r
		self.pi=pi
	def peri(self,r,pi):
		return 2*pi*r
	def area(self,r,pi):
		return pi*r**2
		
r=int(input('Enter the radius:'))
pi=3.14
p=cir(r,pi)
print('The Perimeter is :', p.peri(r,pi))
print('The Area is :', p.area(r,pi))

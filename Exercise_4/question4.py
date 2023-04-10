class rectangle:
    l = 0
    w = 0
    
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def area(self):
        return self.l * self.w
    
    def __str__(self):
        return 'l={} \n w={}'.format(self.l, self.w)

# drive code
l = int(input('Enter length: '))
w = int(input('Enter width: '))
r = rectangle(l, w)
print(r)
print('Area of rectangle is:', r.area())


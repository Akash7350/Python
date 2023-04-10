class Power:
    base = 1
    power = 0
    
    def __init__(self, base, power):
        self.base = base
        self.power = power
        
    def raseto(self):
        return self.base ** self.power
        
    def __str__(self):
        return "base={} \n power={} \n".format(self.base, self.power)    
        
# driver code
base = int(input("Enter the base value : "))
power = int(input("Enter the power value : "))

p = Power(base, power)
print(p)
print('Power is', p.raseto())


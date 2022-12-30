class Numbers:
    MULTIPLIER = 3
    
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        
    def add(self):
        return self.x+self.y
    
    @classmethod
    def multiply(cls, a):
        return cls.MULTIPLIER * a
    
    
    @staticmethod
    def substract(b, c):
        return b-c
    
    @property
    def value(self):
        return(self.x,self.y)
    
    @value.setter
    
    def value(self, xy_tuple):
        self.x,self.y = xy_tuple
        
    @value.deleter
    def value(self):
        del self.x
        del self.y    
          
num  = Numbers(10,15)


print(num.add())
print(num.multiply(2))
print(num.substract(90,23))
#getattr(num.e,num.w)
del num.x
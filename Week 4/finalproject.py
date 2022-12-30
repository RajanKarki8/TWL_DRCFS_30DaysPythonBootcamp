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
    
    
num  = Numbers(10,15)


print(num.add())
print(num.multiply(2))
print(num.substract(90,23))

class test:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):
        return self.a*o.a
        
    
obj1=test(5)
obj2=test(6)
obj3=test("PYTHON  ")
print(test.__add__(obj1,obj2))
print(test.__add__(obj3,obj1))
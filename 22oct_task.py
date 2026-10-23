class A :
    p = 10 
    def __init__(self,b):
        self.var = b

obj = A(99) 
print(id(A.p))  
print(A.p)
print(id(obj.p))
print(obj.p)   


obj.p = 12345

print(A.p)
print(id(A.p))
print(obj.p)
print(id(obj.p))
obj2 = A(33)
print(obj2.p)
print(id(obj2.p))
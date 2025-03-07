#same name with different parameters of same type
class over:
    def s(self, a, b=None): 
        if b is None:
            print(f"One parameter: {a}")
        else:
            print(f"Two parameters: {a}, {b}")

obj = over()
obj.s(100)      
obj.s(100, 200) 
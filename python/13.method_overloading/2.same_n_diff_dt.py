#same name but diff parameters of diff data types
class over2:
    def d(self,a,b=None):
        if b is None:
            print(f"Single parameter: {a}")
        else:
            print(f"Two parameters: {a} and {b}")
obj = over2()
obj.d(10)         
obj.d("welcome")    
obj.d(10, "Hi")
#NoSuchFieldException
'''Python does not have NoSuchFieldException, but we can simulate it using AttributeError'''
class fie:
    def __init__(self):
        self.name = "zoya"

obj = fie()
print(obj.age) 

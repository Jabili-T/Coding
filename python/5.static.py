#ASSIGNMENT-5
#1.accessing through a classs
class static:
    var=14
print("accessing through a class:",static.var)
print("****")
#2.accessing through an instance
obj=static()
print("accessing through an instance: ",obj.var)
print("****")
#3.changing it within an instance
obj.var=20
print("instance var",obj.var)
print("class var",static.var)
print("****")
#4.changing var within the class
static.var=34
print("updated value of class:",static.var)
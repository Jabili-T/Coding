#=================================================ASSIGNMENT-2=====================================
#1.ARITHMETIC OPERATORS
def operations(a,b):
    print("add:",a+b)
    print("sub:",a-b)
    print("multi:",a*b)
    print("division:",a/b)
    print("*********")
#2.INCREMENT AND DECREMENT 
    print("original:",a)
    a+=1
    print("Increment:",a)
    a-=1
    print("Decrement:",a)
    print("*********")
#3.EQUAL OR NOT

    print("EQUAL" if a==b else "NOT EQUAL")
    print("************")
#4.RELATIONAL OPERATORS
    print(a, "<", b, ":", a < b)
    print(a, "<=", b, ":", a <= b)
    print(a, ">", b, ":", a > b)
    print(a, ">=", b, ":", a >= b)
    print("Larger NUM:" ,max(a,b))
    print("SMALLER NUM:" ,min(a,b))
operations(10,20)
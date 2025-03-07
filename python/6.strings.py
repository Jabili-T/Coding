#assignment -6
#diff ways to creating a str
import re
def dif():
    s1="Hello"
    s2='WORLD'
    s3="""welcome to 
    python programming"""
    s4='''Welcome back'''
    print("srting 1:",s1,"srting 2:",s2,"srting 3:",s3,"srting 4:",s4,sep="\n")
    print("****")
#concatenation(+)
    print("concatenation:",s1+" "+s2)
    print("****")
#lenght of str(len)
    print("lenght of string 3:",len(s3))
    print("****")
#str slicing
    print("str slicing from str 4:",s4[2:9])
    print("****")
#searching using index
    print("searching in str using index():",s3.index("o"))
    print("****")
#match()
    s5="welcome"
    print("match():",re.match(s5,s4))
    print("****")
#comparing strings
    print("comparing the str1 and str2:")
    print(s1 == s2)
    print(s1 != s2)
    print("****")
#startswith(),endswith()
    print("startswith(),endswith() using str4 = WELCOME BACK")
    print("startswith():",s1.startswith("welcome"))
    print("endswith:()",s1.endswith("back"))
    print("****")
#trimming str by strip()
    print("strip() in str4:",s4.strip("back"))
    print("****")
#replacing characters in str using replace()
    print("repalcing back with python using replace() in s4 :"+"\n"+s4+"\n"+s4.replace("back","python"))
    print("****")
#splitting by using split()
    print("spliting by using space in s4:",s4.split(" "))
    print("****")
#converting int obj to str
    n=100
    a=str(n)
    print("int obj to str:",a,type((a)))
    print("****")
#upper and lowercase
    print("uppercase for str4:"+s4+"\n"+s4.upper())
    print("lowercase for str4:"+s4+"\n"+s4.lower())
    print("****")
dif()
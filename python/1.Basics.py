#------------------------------------------ASSIGNMENT-1---------------------------------
#1.print ur name
print("TALLURI JABILI")
#2.COMMENTS
#single line
'''****This is the multi-line.
        comments***'''
print("comments in python") # This is inline comment
#3.Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
a = 10
print("Type of a: ", type(a))
b = False
print("Type of b: ", type(b))
c = 5.0
print("Type of c: ", type(c))
S = 'GOOD'
print("Type of S: ", type(S))
#4.Define the local and Global variables with the same name and print both variables and understand the scope of the variables.
a="GLOBAL"
def glo():
    a="LOCAL"
    print("Inside: ",a)
glo()
print("outside: ",a)

#-------------------------------------------------------------ASSIGNMENT-3-----------------------
#---------1.BRIGHT IT CAREER ---10times--for loop
for i in range(1,11):
    print(i ,".","BRIGHT IT CAREER")
print("***************")
#----------2.1 to 20---while loop
i=1
while(i<=20):
    print(i)
    i+=1
print("***************")
#-----------3.(==)and (!=)
a,b=10,15
print("a=",a,"b=",b)
print("a==b:",a==b)
print("a!=b",a!=b)
print("***************")
#-----------4.odd or even
print("Even Numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")

print("\nOdd Numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 != 0:
        print(i, end=" ")
print()
print("******************")
#------------5.Largest number among 3 nums
a,b,c=10,20,30
print("Numbers:",a,b,c)
print("largest num:",max(a,b,c))
print("******************")
#----------6.even numbers---10 to 20 ---while loop
i=10
print("Even numbers from 10 to 20",end="\n")
while i<=20:
    if i%2==0:
        print(i,end=" ")
    i+=1
print()
print("******************")
#----------7.1 to 10 --do while
i=1
while True:
    print(i,end=" ")
    i+=1
    if i>10:
        break
print()
print("******************")
#---------8.ARMSTRONG OR NOT
n=153
d=sum(int(i)**3 for i in str(n))
print("NUM:",n)
print("ARMSTRONG" if d==n else "NOT ARMSTRONG")
print("******************")
#---------9.check num is prime or not
num = int(input("Enter a number to check prime or not: "))
is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
print(num, "is a prime number." if is_prime else "is not a prime number.") 
print("******************")
#----------10.PALINDROME OR NOT
num = input("Enter a number to check palindrome or not: ")
print(num, "is a palindrome." if num == num[::-1] else "is not a palindrome.")
print("******************")
#----------11.even or odd
num = int(input("Enter a number to check even or odd: "))
print("EVEN" if num%2==0 else "ODD")
print("******************")
#-----------12.GENDER M/F
gender = input("Enter M or F: ").upper()
switch = {'M': "Male", 'F': "Female"}
print(switch.get(gender, "Invalid Input"))


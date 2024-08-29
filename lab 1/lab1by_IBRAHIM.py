# python lab 1 by ibrahim saber -------------------:)

#q1

print("Hello words")
#----------------------------------------------------------
# q2 
num1 = input("enter a binary number : ")
num2 = int(num1 , 2)

print(f"you entered {num1} and its = {num2} in decimal")

#----------------------------------------------------------
# q3

num3 = int(input("enter the number u want to check: "))

if num3 % 3 ==0 and num3 % 3 ==0:
    print("FizzBuzz")
elif num3%5 == 0:
    print("buzz")
elif num3%5 == 0 :
    print("Fizz")
else:
    print("the number is not divisible by 3 or 5 try another number :)")


#----------------------------------------------------------
# q4
num4 = float(input("enter the enter the radius: "))

pi = 3.14
area = pi * (num4*num4)
circumference = 2 * pi * num4
if num4 > 0:
    print(f"your radius = {num4} \nThe circle Area = {area} \nThe circle circumference = {circumference}")
else:
    print("The radius should be positive try a number bigger than zero :)")

#----------------------------------------------------------
# q5

name = input("Please enter your name: ")
if name.isalpha() and name.strip():
    email = input("Please enter your email: ")
    print(f"hi {name} \nYour Email is : {email}")
else:
    print("Please enter a valid name .")


#----------------------------------------------------------
# q6

x = input("enter your string: ")

print(x.count("iti"))

#if u want to take the letter u want to cout also from user :)

x = input("enter your string: ")
y = input("enter the word u want to count in the string: ")
print(x.count(y))
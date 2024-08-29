
num1 = input("enter a binary number : ")
for num in num1:
    if num not in ('0', '1'):
        print("please enter 0 or 1 only")
        break
    else:
        num2 = int(num1 , 2)
        print(f"you entered {num1} and its = {num2} in decimal")




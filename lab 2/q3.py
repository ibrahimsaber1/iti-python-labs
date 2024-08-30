#q3 ---------------------- :)

def count_nums():
    count = 0
    arr6 = []
    print("*"*50)
    print("welcom to my code :) u will wnter a set of numbers\nand i will rwturn there total count and avreage :)")
    print("*"*50)
    print("*"*50)
    while True:
        user_num = input("please enter your num: ")
    
        if user_num.lower() == "done":
            
            if count > 0:
                print(f"You Entered => {arr6}")
                print("*"*50)
                print(f"the total number => {sum(arr6)}")
                print("*"*50)
                print(f"the Avrage => {sum(arr6)/count}")
                print("*"*50)
                print("thank u for using this code")
            else:
                print("u did not add any numbers :(")
            
            break
        else:
            try:
                num6 = float(user_num)
                arr6.append(num6)
                count +=1
            except :
                print("Invalid input. Please enter a number")
                continue

count_nums()

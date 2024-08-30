#q1 ---------------------- :)

def sory_arr():
    arr1 = []
    for i in range(5):
        num = int(input(f"pleas enter number {i+1} : "))
        arr1.append(num)

    print(f"you entered => {arr1}")
    arr2 = sorted(arr1)
    print(f"the ascending order =>  {arr2}")
    arr3 = sorted(arr1,reverse=True)
    print(f"the descnding order =>  {arr3}")
    

sory_arr()
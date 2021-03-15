largest = None
smallest = None

while True:
    snum = input("Enter a number :")
    if snum == "done":
        break
    try:
        num = int (snum)
    except:
        print("Invalid input")

    if largest is None :
        largest = num
    elif largest < num :
        largest = num

    if smallest is None :
        smallest = num
    elif smallest > num :
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)

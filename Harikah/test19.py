def emplist ():
    empdict = {}
    empdata = []
    i = 1
    dictlen = int(input('enter the number of employees :'))
    while i <= dictlen:
        name = input('enter the name :')
        age = input('enter the age :')
        gender = input('enter the gender :')
        address = input('enter the address :')
        empdict[i] = [name, age, gender, address]
        i=i+1
    for keys,values in empdict.items(): 
        print(keys) 
        print(values)


emplist()
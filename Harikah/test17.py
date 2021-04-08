
a=(10,20,30,40)

a=list(a)
a.insert(3,'azure')
a=tuple(a)
print(a,type(a))

employees={10:"Ram",20:"Rani",30:"Pinky",50:"Amar"}


print(employees[20])

employees[60]='Nair'
print(employees)

employees[10]='Krishna'
print(employees)

del employees[60]
print(employees)

print(employees.keys())
print(employees.values())
print(employees.items())


a={10:"john",20:"Peter",30:"Mic"}
b={100:"Raj",200:"Reya"}
b.update(a)
print(b)


employeee1=employees.copy()
print(employeee1)

employees.clear()
print(employees)

del(employees)
print(employees)


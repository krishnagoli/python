x=['unix','linux','perl','python','java','perl','aws','linux','devops']

def line():
    line='*'*40
    print(line)

x.append('azure')
print(x)

line()

x.remove('azure')
print(x)

line()

y=['azure','gcp']
x.extend(y)
print(x)

line()

del x[9::]
print(x)

line()

x.insert(3,'azure')
print(x)

line()

x.pop()
print(x)

line()

x.append('devops')
print(x)

line()

x.pop(3)
print(x)

line()

print(x.count('aws'))

line()

x.reverse()
print(x)
x.reverse()

line()

x.sort()
print(x)

line()

y=sorted(x,reverse=True)
print(y)
print(x)

line()

print(x.index('linux'))

line()

print(len(x))

line()

y=[100,150,50,80,200,300]
print(max(y))
print(min(y))
print(sum(y))

line()

for count, x in enumerate(x):
    print(count,x)

line()

list1=[33,22,11]
list2=[11,44,55,22]
finallist=list1+list2
print(finallist)

line()

x=[i**2 for i in range(200,301)]
print(x)

line()

x=[i**3 for i in range(500,901) if i%2!=0]
print(x)

line()



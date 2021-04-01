x=['unix','linux','perl','python','java','perl','aws','linux','devops']

x.append('azure')
print(x)

x.remove('azure')
print(x)

y=['azure','gcp']
x.extend(y)
print(x)

del x[9::]
print(x)

x.insert(3,'azure')
print(x)

x.pop()
print(x)

x.append('devops')
print(x)

x.pop(3)
print(x)

print(x.count('aws'))

x.reverse()
print(x)
x.reverse()

x.sort()
print(x)

y=sorted(x,reverse=True)
print(y)
print(x)

print(x.index('linux'))


def square(a):
    squareunit = input('enter the square measurement unit:')
#    a = int(input('enter the length of a side of the square:'))
    area=a**2
    print('Area of the square with each side of {}{} is {}{}'.format(a,squareunit,area,squareunit))

def triangle(x,y,z):
    triunit =  input('enter the triangle measurement unit:')
    perimeter = x+y+z
    print('Perimeter of the triangle with sides of {}{},{}{},{}{} is {}{}'.format(x,triunit,y,triunit,z,triunit,perimeter,triunit))

square(5)
triangle(1,2,3)

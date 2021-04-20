numa = int(input('enter first number :'))
numb = int(input('enter second number :'))

add = numa + numb
sub = numa - numb
mul = numa * numb
div = numa / numb
mod = numa % numb

print('Sum of {} and {} is {}'.format(numa, numb, add))
print('Difference of {} and {} is {}'.format(numa, numb, sub))
print('Product of {} and {} is {}'.format(numa, numb, mul))
print('Division of {} and {} is {}'.format(numa, numb, div))
print('Modulus of {} and {} is {}'.format(numa, numb, mod))

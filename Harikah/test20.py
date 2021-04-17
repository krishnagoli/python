def add(numa,numb):
    add = numa + numb
    print('Sum of {} and {} is {}'.format(numa,numb,add))

def sub(numa,numb):
    sub = numa - numb
    print('Difference of {} and {} is {}'.format(numa,numb,sub))

def mul(numa,numb):
    mul = numa * numb
    print('Product of {} and {} is {}'.format(numa,numb,mul))

def div(numa,numb):
    div = numa / numb
    print('Division of {} and {} is {}'.format(numa,numb,div))


while input('Do you want to prform arithmetic operations (yes or no):')=='yes':
    numa = int(input('enter first number :'))
    numb = int(input('enter second number :'))
    add(numa,numb)
    sub(numa,numb)
    mul(numa,numb)
    div(numa,numb)
else:
    print('thank you. hope you enjoyed')

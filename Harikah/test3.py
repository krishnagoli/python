item1, cost1 = input('Enter the name and cost of first item seperated by comma').split(',')
item2, cost2 = input('Enter the name and cost of second item seperated by comma').split(',')
item3, cost3 = input('Enter the name and cost of third item seperated by comma').split(',')

cost1=float(cost1)
cost2=float(cost2)
cost3=float(cost3)

avgcost = (cost1+cost2+cost3)/3

print('the average cost of {}, {} and {} is £{}'.format(item1, item2, item3, avgcost))
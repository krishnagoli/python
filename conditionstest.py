hrs = input("Enter Hours :")
rate = input("Enter Rate per hour :")

hrs = float(hrs)
rate = float(rate)

if hrs<=40:
   pay = hrs*rate
   print (pay)
else:
   pay = (hrs-40)*(rate*1.5) + 40*rate
   print (pay)

print("you are the best")

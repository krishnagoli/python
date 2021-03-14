hrs = input("Enter Hours :")
rate = input("Enter Rate per hour :")
try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print("Error, please enter numberic value")
    quit()

def computepay(hrs,rate):
    if hrs<=40:
       pay = hrs*rate
    else:
       pay = (hrs-40)*(rate*1.5) + 40*rate
    return pay

pay = computepay(hrs,rate)

print("Pay",pay)

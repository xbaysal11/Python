
bal = int(input())
anInt= float(input())

monInt = anInt/12.0
high_b = (bal * (1 + monInt)**12)/12.0
low_b = bal/12
fixedPayment2 = (high_b + low_b)/2

def remain(bal,monInt,fixedPayment2):
    month = 1
    while month <= 12:
        bal -=  fixedPayment2 
        bal += monInt*bal
        month += 1
    return bal

while 2**2 == 4 :
    x = remain(bal,monInt,fixedPayment2)
    if  round(x) < 0:
        high_b = fixedPayment2
        fixedPayment2 = (high_b + low_b)/2
    elif round(x) > 0:
        low_b = fixedPayment2
        fixedPayment2 = (high_b + low_b)/2
    elif round(x) == 0:
        print 'Lowest Payment:',round(fixedPayment2,2)
        break	 	  	 	  	   	  	     	     	 	

fixedPayment1 = 0

bal = int(input("Balance as a polynomial: "))
anInt = int(input("AnnualInterestRate as a decimal: "))

def remain(bal,anInt,fixedPayment1):
    
    month = 1
    while month <= 12:
        bal -=  fixedPayment1 
        bal += (anInt/12.0)*bal
        month += 1
        
    if bal <= 0:
        return fixedPayment1
    else:
        return False

while 2*2 == 4 :
    
    if remain(bal,anInt,fixedPayment1):
        print 'Lowest Payment:',remain(bal,anInt,fixedPayment1)
        break
    else:
        fixedPayment1 += 10
        remain(bal,anInt,fixedPayment1)
	 	  	 	  	   	  	     	     	 	

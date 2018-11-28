##Problem1: PAYING THE MINIMUM  

def problem1(bal,anInt,monPay):
    
    print('MonthBalance    Minimum Payment    Total Paid    Interest')
    
    total = 0
    month = 0
    
    while month <= 11:
        
        mPay = bal * monPay
        bal -= mPay
        bal += anInt / 12.0 * bal
        total += mPay
        month+=1
        x = 2
        print(str(month)+'    '+str(round(bal, 2))+'   '+str(round(mPay, 2))+'         '+str(round(total, 2))+'       '+str(round((anInt / 12.0 * bal), 2)))
                    
bal = int(input('Annual balance as a polynomial: '))
anInt = float(input('Annual credit card interest rate as a decimal: '))
monPay = float(input('Minimum monthly payment rate as a decimal: '))

problem1(bal,anInt,monPay)

	 	  	 	  	   	  	     	     	 	

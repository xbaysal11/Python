a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a < b  and a < c :
  	print("The least of these three numbers is: ", a)
if b < a  and b < c:
    print("The least of these three numbers is: ", b)
if c < a  and c < b:
    print("The least of these three numbers is: ", c)
    
    
if a < b == c or a < c == b:
  	print("The least of these three numbers is: ", a)
if b < a == c or b < c == a:
    print("The least of these three numbers is: ", b)
if c < a == b or c < b== a:
    print("The least of these three numbers is: ", c)
    
if a > b == c or a > c == b:
  	print("The least of these three numbers is: ", c)
if b > a == c or b > c == a:
    print("The least of these three numbers is: ", a)
if c > a == b or c > b== a:
    print("The least of these three numbers is: ", b)
elif a == b and a  ==  c and b == c:
		print("They are all equal")
 	 	  	 	  	   	  	     	     	 	

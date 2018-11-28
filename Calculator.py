
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operator = (input("Enter an operator: "))
def choose():
    if operator == 'add':
       print('Result is '+ str(number1 + number2)+',')
    elif operator == 'subtract':
       print('Result is '+ str(number1 - number2)+',')
    elif operator == 'multiply':
        print('Result is '+ str(number1 * number2)+',')
    elif operator == 'divide': 
        print('Result is '+ str(number1 / number2)+',')
    else:
        if number2 == 0:
            print("Division by 0")
        else:
            print('Result is '+ str(number1 / number2)+',')
choose()

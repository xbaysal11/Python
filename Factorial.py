n = int(input('Enter a number: '))
if n < 0:
    print('Negative integer.')
else:    
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
    print('Factorial of ' + str(n) + ' is ' + str(fact))
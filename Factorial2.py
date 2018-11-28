from math import factorial

a = input()

if a<0:
    print('error')
elif type(a)==str:
    print('error')
else:
    print(factorial(a))
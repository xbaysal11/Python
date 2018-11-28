y = int(input('year: '))
if y < 0:
    print('invalid input')
elif y % 4 == 0:
    print('This is a leap year')
elif y%4 !=0:
    print('This is not a leap year')
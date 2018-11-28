def celsius_to_fahrenheit(x):
    return 1.8 * x + 32

def fahrenheit_to_celsius(x):
    return (5/9) * (x - 32)

y = input()
x = int(input())

if y == 'f' or y == 'F':
  print ("'" + str(x) +" C = " + str(int(celsius_to_fahrenheit(x)))+" F" + "'")
elif y == 'c' or y == 'C':
  print (x, 'F =', fahrenheit_to_celsius(x), 'C')
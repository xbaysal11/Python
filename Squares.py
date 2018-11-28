from __future__ import print_function
n = int(input(''))
for i in range(1,n+1):
    print(i**2, end = ', ')
for i in range(0, -n+1):
    print(i**2, end = ', ')
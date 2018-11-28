from __future__ import print_function
num = int(input(''))
count = 0
for j in range(1, num + 1):
    if j % 5 == 0 or j % 7 == 0:
        print(j, end=',')
        count += 1
print("\nThere are", count , "numbers divisible by 5 or 7.")

num = int(input('Enter a number: '))
sum = 0
i = 2
for i in range(num+1):
    sum = (sum+(2**i))
print('The sum is '+ str(sum))

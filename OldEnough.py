n = int(input("Age:"))
if n > 18 and n < 150:
    print("Old enough!")
elif n >= 0 and n <= 18:
    print("Too young. ")
else:
    print("Incorrect age.")
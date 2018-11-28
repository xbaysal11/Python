a = int(input(""))
b = int(input(""))
c = int(input(""))
if a == 0 or b == 0 or c == 0:
    print("It is not a valid triangle.")
elif a + b + c == 180:
    print("It is a valid triangle.")
else:
    print("It is not a valid triangle.")
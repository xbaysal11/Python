time = int(input(""))
if time >= 0 and time <= 5:
    print("Good night!")
elif time >= 6 and time <= 9:
    print("Good morning!")
elif time >= 10 and time <= 19:
    print ("Good day!")
elif time >= 20 and time <= 24:
    print ("Good evening!")
else:
    print ("Not acceptable time.")

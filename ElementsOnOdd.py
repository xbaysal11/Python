def odd(t1):
    if len(t1) == 1:
        print(t1[0])
    else:
        print(t1[0::2])
t1 = input()
odd(t1)
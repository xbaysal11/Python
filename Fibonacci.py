t1 = []
def f(x):
    a,b = 0,1
    for i in range (0,x):
        a,b = b,a+b
        t1.append(a)
    return t1
x = input()
print(f(x))
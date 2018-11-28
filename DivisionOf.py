x = int(input())
y = int(input())
if x==0 or y==0:
        print("Division by 0")
else:
    def add(x,y):
        c = x / y
        return c
    res = add(x,y)
    print(res)
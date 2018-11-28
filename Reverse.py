def isReverse(x,y):
    if x==y[::-1]:
        return("True")
    else:
        return("False")
x=input()
y=input()
print(isReverse(x,y))
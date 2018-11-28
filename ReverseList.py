def rev(a):
    if len(a) == 1:
        return (a[0])
    else:
        return (a[::-1])
a = input()
print(rev(a))
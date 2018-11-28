def clip(lo, x, hi):
    x = max(lo, x)
    x = min(x, hi)   
    return x

lo = int(input())
x = int(input())
hi = int(input())
print (clip(lo, x, hi))

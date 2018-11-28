def odd(x):

    '''

    x: int or float.

    returns: True if x is odd, False otherwise

    '''

    if x%2 == 0 :
         return ("False")
    else:
         return("True")

x = int(input())
print(odd(x))
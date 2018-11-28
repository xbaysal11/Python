def rectangle_area(x, y):
    if x <= 0 or y <= 0:
        print("Incorrect input!")
    else:
        print(x*y)
    ''' num, num -> num
    Returns the area of the rectangle with dimensions:width & height
    >>> rectangle_area(4,5)
    20

    '''
x = int(input())
y = int(input())

rectangle_area(x, y)
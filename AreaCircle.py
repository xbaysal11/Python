def circle_area(radius):
    
    if radius <= 0 :
        print("Incorrect input!")
    else:
        print(radius*radius*3.14)
        
    ''' num -> num

   Returns the area of the circle with the entered radius. Take pi = 3,14.

   >>> circle_area(4)

   50,24

   '''
radius = int(input())

circle_area(radius)
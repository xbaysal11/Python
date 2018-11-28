def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):

    radiation = 0
    count = start
    while count < stop:        
        radiation += step * f(count)
        count += step
    return radiation
start = raw_input()
stop = raw_input()
step = input()
print radiationExposure(start, stop, step)

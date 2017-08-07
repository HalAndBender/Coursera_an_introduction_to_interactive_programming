import math

def polygon(sides,length):
    area =  (sides * length**2)/(4*math.tan(math.pi/sides))
    return area

print ((polygon(5,7)))
print ((polygon(7,3)))
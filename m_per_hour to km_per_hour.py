from math import pi


pi=3.14
h=float(input('enter the height:',))
r=float(input('enter the radius:',))

LaterArea=2*pi*r*h
TotalArea=((2*pi)*(r**2))+(LaterArea)
Volume=(pi*h*(r**2))


print('The LaterArea of Cylinder is:', LaterArea)
print('The TotalArea of Cylinder is:', TotalArea)
print('The Volume of Cylinder is:', Volume)
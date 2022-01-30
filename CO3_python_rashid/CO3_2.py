from GRAPHICS import rectangle
from GRAPHICS import circle
from GRAPHICS.ThreeD_graphics import cuboid
from GRAPHICS.ThreeD_graphics import sphere

l=int(input("Enter the length of rectangle: "))
b=int(input("Enter the breath of rectangle: "))
rectangle.area(l,b)
rectangle.perimeter(l,b)
print()
r=int(input("Enter the Radius of Circle: "))
circle.area(r)
circle.perimeter(r)
print()
l=int(input("Enter the length of Cuboid: "))
b=int(input("Enter the breadth of Cuboid: "))
h=int(input("Enter the height of Cuboid: "))
cuboid.area(l,b,h)
cuboid.perimeter(l,b,h)
print()
r=int(input("Enter the radius of Sphere: "))
sphere.area(r)
sphere.volume(r)

class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return 2*self.breadth+self.length

a1=int(input("Enter length of rectangle: "))
b1=int(input("Enter breadth of rectangle: "))
obj1=rectangle(a1,b1)
print("Area of rectangle:",obj1.area())
print("perimeter of rectangle:",obj1.perimeter())
a2=int(input("Enter length of rectangle: "))
b2=int(input("Enter breadth of rectangle: "))
obj2=rectangle(a2,b2)
print("Area of rectangle:",obj2.area())
print("perimeter of rectangle:",obj2.perimeter())
if (obj1.area()>obj2.area()):
    print("object 1 is greater")
else:
    print("object 2 is greater")
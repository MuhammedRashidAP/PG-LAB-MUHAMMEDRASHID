class rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def __lt__(self,a1):
        area1=self.__length*self.__width
        area2=a1.__length*a1.__width
        if(area2<area1):
            return(True)
        else:
            return(False)  
a1=int(input("Length of  first rectangle:"))
b1=int(input("width  of first rectangle:"))
r1=rectangle(a1,b1)
a2=int(input("Length of second rectangle:"))
b2=int(input("width of second rectangle:"))
r2=rectangle(a2,b2)
if(r1<r2):
    print("First Rectangle  is larger!!")
else:
    print("Second Rectangle is larger!!")

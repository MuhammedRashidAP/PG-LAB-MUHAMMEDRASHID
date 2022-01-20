class Time:

    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second

    def __add__(self,h):
        second=self.__second+h.__second
        minute=self.__minute+h.__minute
        hour=self.__hour+h.__hour
        if(second>60):
            second=second-60
            minute=minute+1
        if(minute>60):
            minute=minute-60
            hour=hour+1
        return hour,minute,second

print("Enter first time:")
h1=int(input("enter the hour:"))
m1=int(input("enter the minute:"))
s1=int(input(" enter the second:"))
t1=Time(h1,m1,s1)
print("The first time is ",end=":")
print(h1,":",m1,":",s1)
print("Enter  second time:")
h2=int(input("enter the hour:"))
m2=int(input("enter the minute:"))
s2=int(input("enter the second:"))
print("The second time is ",end=":")
print(h2,":",m2,":",s2)
t2=Time(h2,m2,s2)
hr,min,sec=t1+t2
print("The added time is ",end=":")
print(hr,end=":")
print(min,end=":")
print(sec,end=" ")
print("\n")
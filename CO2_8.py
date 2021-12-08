a=[]
n=int(input("enter the number of element in list:"))
for x in range(0,n):
    element=input("enter element"+str(x+1))
    a.append(element)
    max1=len(a[0])
    temp=a[0]
for i in a:
    if(len(i)>max1):
        max1=len(i)
        temp=i
print("longest word:",temp)
print("length of longest word:",max1) 
        
    

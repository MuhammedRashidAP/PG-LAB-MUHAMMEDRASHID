l=[1,3,5,7,9,11,34]
l1=[5,13,45,7,20,65,1]
s=int(0)
c=int(0)
if len(l)==len(l1):
    print("list are of same length")
else:
    print("list are of same length")
for i in range(0,len(l) and len(l1)):
               s=s+l[i]
               c=c+l1[i]
if(s==c):
    print("equal sum")
else:
    print("not equal sum")
print("elements that matched are:")
I=[]
for i in range(0,len(l)):
    for j in range(0,len(l1)):
        if l[i]==l1[j]:
            I.append(l[i] and l1[j])
        else:
            continue
print(I)
    
            
    
        
               

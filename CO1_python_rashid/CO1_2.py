s=int(input("enter strat year"))
e=int(input("enter end year"))
if(s<e):
    print(" leap year are:",end=" ")
    for i in range(s,e):
        if i%4==0 and i%100!=0:
            print(i,end=" ")
            

n=[]
s=int(input(" enter a limit"))
print("enter ",s," values")
for i in range(0,s):
    n.append(int(input()))
print("\n the list after assinging: \n")
for i in range(0,len(n)):
    if n[i]>=100:
        print("over")
    else:
        print(n[i])

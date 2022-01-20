f1=open("firstfile.txt","r")
for x in f1:
    print(x)
f1.seek(0,0)
print()
print("....................................")
f2=open("odd.txt","w")
ff=f1.readlines()

with open('odd.txt','w') as f2:
    for x in range(0,len(ff)):
        if(x%2!=0):
            print(ff[x])
            f2.write(ff[x])
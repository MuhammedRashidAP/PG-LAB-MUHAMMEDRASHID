test=str(input("enter the string"))
freq={}
for i in test:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("count of all characters:"+str(freq))

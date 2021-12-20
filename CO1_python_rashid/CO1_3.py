list1=[-10,20,35,-67,70]
re=[num for num in list1 if num>=0]
print(re)
print("\n .................................   ")
n=int(input("enter limit:"))
squarelist=[i**2 for i in range(1,n+1)]
print("square of n numbers:",squarelist)

print("\n .................................   ")
word=str(input("enter the word"))
print("the original string is:"+word)
print(" the vowels are",end=" ")
for i in word:
    if i in 'aeiouAEIOU':
        print([i],end=" ")
print("\n .................................   ")
w=input("enter the word:")
print("ordinal value corresponding to each element is ")
for i in w:
    print(i,end=":")
    print(ord(i),end=" ")
    

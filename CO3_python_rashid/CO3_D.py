import random
mylist = ["muhammed rashid", "nishan", "athul"] 
print(random.choice(mylist))
print(random.choices(mylist, k=4))
print(random.sample(mylist, k=1))
random.shuffle(mylist)
print(mylist)
print(random.randrange(3, 9))

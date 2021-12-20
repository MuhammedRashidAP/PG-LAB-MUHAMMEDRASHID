import random
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
print("*************")
import random  
random.seed(5)  
print(random.random())
print(random.random())
print("***********")
import random  
r1 = random.randint(5, 15)
print("Random number between 5 and 15 is % s" % (r1))  
r2 = random.randint(-10, -2)
print("Random number between -10 and -2 is % d" % (r2))
print("**************")
import random
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
string = "geeks"
print(random.choice(string))  
tuple1 = (1, 2, 3, 4, 5)
print(random.choice(tuple1))

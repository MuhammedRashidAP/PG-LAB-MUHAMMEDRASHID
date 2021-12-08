str=input("enter a string")
print("inputed string is:",str)
if(str.endswith("ing")):
    str=str+'iy'
else:
    str=str+'ing'
print("the formatted string is:",str)

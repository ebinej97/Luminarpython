import re
x='\d{10}'
vname=input("enter the variable name ")

match=re.fullmatch(x,vname)
if(match!=None):
    print("Valid")
else:
    print("invalid variable name")
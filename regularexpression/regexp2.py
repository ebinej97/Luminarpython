#rules
#a,,,,k
#it should be a digit and / by 3
#any characters
import re
x='[a-k][369][a-z]*'
vname=input("enter the variable name ")

match=re.fullmatch(x,vname)
if(match!=None):
    print("Valid")
else:
    print("invalid variable name")
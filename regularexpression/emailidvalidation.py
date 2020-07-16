import re
x='[a-zA-Z][a-zA-Z0-9]\w*@gmail[.]com'
vname=input("enter the variable name ")

match=re.fullmatch(x,vname)
if(match!=None):
    print("Valid")
else:
    print("invalid variable name")
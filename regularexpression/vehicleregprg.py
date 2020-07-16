import re
x='kl\d{2}[a-z]{2}\d{4}'
vname=input("enter the variable name ")

match=re.fullmatch(x,vname)
if(match!=None):
    print("Valid")
else:
    print("invalid variable name")


# kl08av8730
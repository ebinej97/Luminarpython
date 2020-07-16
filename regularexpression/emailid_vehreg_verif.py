import re
f=open("emailidverif","r")
f2=open("validmailid_vehreg", "w")
f3=open("vehicleregdata","r")
x='[a-zA-Z][a-zA-Z0-9]\w*@gmail[.]com'
f2.write("*******EMAIL ID********")
for i in f:
    i=i.rstrip("\n")
    match=re.fullmatch(x,i)
    if(match!=None):
        f2.write("\n")
        f2.write(i)
        f2.write("\n")
    else:
        pass
y='kl\d{2}[a-z]{2}\d{4}'
f2.write("*******VEHICLE REGISTRATION*********")
for i in f3:
    i=i.rstrip("\n")
    match=re.fullmatch(y,i)
    if(match!=None):
        f2.write("\n")
        f2.write(i)
        f2.write("\n")
    else:
        pass

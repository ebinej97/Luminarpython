f=open("abc.txt","r")
fw=open("evenno.txt","w")
for data in f:
    even=int(data)
    if(even%2==0):
        fw.write(str(even)+"\n")

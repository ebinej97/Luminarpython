# f=open("class.txt","r")
# f2=open("passed.txt","r")
# f3=open("result.txt","w")
# for name in f:
#     if name not in f2:
#         f3.write(name+"\n")


#using function
f1=open("class.txt","r")
f2=open("passed.txt","r")
f3=open("fail.txt","w")
st1=set()
st2=set()

def readDataFromFile(fref):
    st=set()
    for data in fref:
        data=data.rstrip("\n")
        st.add(data)
    return st
st1=readDataFromFile(f1)
st2=readDataFromFile(f2)
print(st1)
print(st2)
fail=st1-st2
print(fail)
for data in fail:
    f3.write(data+"\n")
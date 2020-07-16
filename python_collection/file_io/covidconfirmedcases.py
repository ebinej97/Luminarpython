
f=open("C:/Users/Ebin/PycharmProject/luminartech/python_collection/file_io/complete.csv","r")
dict={}
dict2={}
for lines in f:
    report=lines.rstrip("/n").split(",")
    state=report[1]
    cases=int(report[4])
    if state not in dict:
        dict[state]=cases
    else:
        dict[state]=cases
print(dict)
total=0
srtlst=[]
for k,v in dict.items():
    srtlst.append((v,k))
print("=======Sorted Data=======")
print(srtlst)
sorteddata=sorted(srtlst,reverse=True)
print("======3highest cases confirmed states======")
print(sorteddata[:3])

for k,v in dict.items():
    total+=v
print("Total Confirmed cases =>",total)




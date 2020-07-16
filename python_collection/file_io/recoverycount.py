#list out the recovered list and find the state with highest recovery
f=open("C:/Users/Ebin/PycharmProject/luminartech/python_collection/file_io/complete.csv","r")
dict={}
for lines in f:
    report2=lines.rstrip("/n").split(",")
    state=report2[1]
    recover=int(report2[6])
    if state not in dict:
        dict[state]=recover
    else:
        dict[state]=recover
print("=======Recovery list state wise=======")
print(dict)
stlst=[]
for k,v in dict.items():
    stlst.append((v,k))
    stlst=sorted(stlst,reverse=True)

print("==========Sorted List===========")
print(stlst)
print("=========================================="
      "==========================================")
print("State with highest recovery is =>",stlst[0])


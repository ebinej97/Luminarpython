f=open("C:/Users/Ebin/PycharmProject/luminartech/python_collection/file_io/complete.csv","r")
dict={}
for lines in f:
    report=lines.rstrip("/n").split(",")
    state=report[1]
    cases=int(report[4])
    if state not in dict:
        dict[state]=cases
    else:
        dict[state]=cases
print(dict)
import matplotlib.pyplot as plt
total=0
stlst=[]
state=[]
cnfd=[]
for k,v in dict.items():
    stlst.append((v,k))
    stlst=sorted(stlst,reverse=True)
    report=stlst[:3]
print(report)

for values in report:
    cnfd.append(values[0])
    state.append(values[1])
plt.bar(state,cnfd)
plt.show()

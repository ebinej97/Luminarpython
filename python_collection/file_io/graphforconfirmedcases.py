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
import matplotlib.pyplot as plt
states=[]
cnt=[]
for k,v in dict.items():
    states.append(k)
    cnt.append(v)
plt.bar(states,cnt)
plt.show()




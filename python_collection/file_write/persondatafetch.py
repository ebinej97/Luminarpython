f=open("person.txt","r")
emp={}

for data in f:
    values=data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    age=values[2]
    desig=values[3]
    exp=values[4]
    salary=values[5]
    if(id not in emp):
        emp[id]={"id":id,"name":name,"desig":desig,"exp":exp,"salary":salary}
    else:
        pass
for k,v in emp.items():
    print(k,"\t",v)



def printEmployee(**kwargs):


    prop=kwargs["property"]
    id=kwargs["id"]
    print(emp[id]["name"])
    # print(emp[id][prop])
    print(emp[id]["exp"])
    #print(id,"\t",prop)

printEmployee(id="101",property="desig")


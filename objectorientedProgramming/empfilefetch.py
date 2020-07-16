class Employee:
    def __init__(self,eid,name,desig,sal,exp):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.sal=sal
        self.exp=exp
    def printemp(self):
        print(self.eid,",",self.name,",",self.desig)
f=open("emp")
emp=[]
for data in f:
    employees=data.rstrip("\n").split(",")
    eid=employees[0]
    name=employees[1]
    desig=employees[2]
    sal=int(employees[3])
    exp=employees[4]
    ob=Employee(eid,name,desig,sal,exp)
    ob.printemp()
    emp.append(ob)
for employee in emp:
    if(employee.sal>17000):
        print(employee.name)


for employee in emp:
    name=employee.name
    print(name.upper())
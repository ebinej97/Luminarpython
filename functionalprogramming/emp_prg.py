#convert all emp name to upper case
#print all emp salary greater than 15000
# provide increment for all emp who have exp >=2  increment of 5000
#list all emp desig =developer
class employee:
    def __init__(self,id,name,desig,salary,exp):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=int(salary)
        self.exp=exp

lst=[]
f=open("employee")
for data in f:
    words=data.rstrip("\n").split(",")
    id=words[0]
    name=words[1]
    desig=words[2]
    salary=int(words[3])
    exp=int(words[4])
    ob=employee(id,name,desig,salary,exp)
    lst.append(ob)
upperlst=list(map(lambda employee:employee.name.upper(),lst))
print(upperlst)


#emp sal greater than 15000
sal=list(filter(lambda employee:employee.salary>15000,lst))
for val in sal:
    print(val.name)
inc=list(filter(lambda employee:employee.exp>2,lst))
for val in inc:
    val.salary+=5000
    print(val.name,val.salary)


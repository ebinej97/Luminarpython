#prg to print emp name, id,desig,comname,salary
class employee:
    def getvalues(self,ename,id,desig,cname,salary):
        self.ename=ename
        self.id=id
        self.desig=desig
        self.cname=cname
        self.salary=salary

    def printvalues(self):
        print("Name:",self.ename)
        print("ID:",self.id)
        print("Desig:",self.desig)
        print("Company Name:",self.cname)
        print("Salary:",self.salary)
emp=employee()
emp.getvalues("John",8902,"Team Lead","Tech Mahindra",35000)
emp.printvalues()
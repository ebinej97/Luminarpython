#class
#object
#refrence
#class ->plan,design pattern,blue print

#object relworld entity
#
#class ClassName:
# methods


class Person:

    def setvalues(self,age,name):
        self.name=name
        self.age=age
    def printvalues(self):
        print("name is",self.name)
        print("age is",self.age)
ob=Person()
ob.setvalues(25,"ajay")
ob.printvalues()



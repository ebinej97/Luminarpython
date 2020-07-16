class student:
    def __init__(self,name,rol,course):
        self.name=name
        self.rol=rol
        self.course=course
    def printvalues(self):
        print(self.name,",",self.rol,",",self.course)
ob=student("ajay",1001,"mca")
ob.printvalues()
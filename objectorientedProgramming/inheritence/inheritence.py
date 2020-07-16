#inheritance means to inherit the properties of parent class

class  parent:
    def phone(self):
        print("parent have nokia phone")

class child(parent):
    def phone2(self):
        print("child have iphone")
        
p=parent()
p.phone()
p.phone2()
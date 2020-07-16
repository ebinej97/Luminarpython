#polymorphism many types
#method overloading
#method overriding
#operator overloading

#method overloading
#same method name and different number of arguments
#python does not support overloading directly so only the recent one will be executed
class mathsop:
    def add(self):
        print("inside no arg method")
    def add(self,num1):
        print("inside singlw=e arg method")
    def add(self,num1,num2):         #only this recent one will be executed
        print("inside two arg method")

ob=mathsop()
ob.add(10,20)
# ob.add()
# ob.add(40)


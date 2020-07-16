class p1:
    def m1(self):
        print("inside parent 1")
class p2(p1):
    def m2(self):
        print("inside parent 2")
class p3(p2):
    def m3(self):
        print("inside parent 3")
ob=p3()
ob.m3()
ob.m2()
ob.m1()

ob2=p2()
ob2.m3()
ob2.m2()
ob2.m1()

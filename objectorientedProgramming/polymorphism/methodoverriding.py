#if two classes have same attribute but different property the method will be overrided
class parent:
    def phone(self):
        print("parent have phone")
class child(parent):
    def phone(self):
        print("i have iphone")
ob=child()
ob.phone()
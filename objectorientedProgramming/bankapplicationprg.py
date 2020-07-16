
class bank:
    self.bname = "SBI"  #static variable ,declared in class for memory efficiency
    def create(self,acno,actype,pname): #local variable
        self.acno=acno      #instance variable
        self.actype=actype
        self.pname=pname
        self.balance=3000
    def deposit(self,amount):
        self.balance+=amount
        print("your",self.bname,"account has been credited with amount",amount)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance in your account!transaction has been cancelled")
        else:
            self.balance-=amount
            print("Your",self.bname,"account has been debited with amount",amount)
    def enquiry(self):
        print("Your available balance is :",self.balance)
b=bank()
b.create(1234,"savings","Ebin")
b.deposit(4000)
b.withdraw(7000)
b.enquiry()

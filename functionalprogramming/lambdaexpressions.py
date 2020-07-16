#anonymous expression => nameless
#
# def add(num1,num2):
#     return(num1+num2)
f1=lambda num1,num2:(num1+num2)
f2=lambda num1,num2:(num1-num2)
f3=lambda num1,num2:(num1*num2)
f4=lambda num1,num2:(num1/num2)
print(f1(10,20))
print(f2(20,10))
print(f3(20,10))
print(f4(20,10))

sq=lambda num1:(num1**2)
print(sq(10))
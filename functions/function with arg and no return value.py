#function with argument and no return value
#syntax
    #def functioname(arg1,arg2,.....argn):
    #function body

# def add(num1,num2):
#     print(num1+num2)
# def mul(num1,num2):
#     print(num1*num2)
# add(20,10)
# mul(20,10)
#prg to create a fun to check the given number odd or not
# def check(num):
#     if(num%2==0):
#         print(num,"is even")
#     else:
#         print(num,"is odd")
# check(12)

#create a function to check given no is prime or not

def prime(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
        else:
            pass
    if(flag==1):
        print(n,"is not a prime")
    else:
        print(n,"is a prime")
n=int(input("Enter the number"))
prime(n)




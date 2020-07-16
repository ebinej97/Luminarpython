#try -dobtful code
# except - handling code
#finally- for clearing processing


#exception as function

num1=int(input("Enter the num1"))
num2=int(input("Enter the num2"))
try:
    sum=num1/num2
except Exception as e:
    print(e.args)
#raise
#
#
# age=int(input("enter the age"))
#
# if(age<18):
#     raise Exception("Invalid age")
# else:
#     print("you can vote")
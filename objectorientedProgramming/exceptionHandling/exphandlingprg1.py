# num1=int(input("enter no1"))
# num2=int(input("enter no2"))
# indx=int(input("Enter index position to fetch element"))
# lst=[10,20,30]
# try:
#     res=num1/num2
#     print("Result is ",res)
#     print(lst[indx])
#
# except Exception as e:
#     print(e.args) #exception occured
#     num2=int(input("Enter value for num2"))
#     res=num1/num2
#     print("RESULT",res)
#
#
# finally:
#
#     print("i have file operation")


#raise    => can be used to customize user specified exceptions
age=int(input("Enter the age"))

if(age<18):
    raise Exception("Invalid age")

else:
    print("u can vote")



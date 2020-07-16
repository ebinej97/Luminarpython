#num=int(input("enter the number"))
#if(num>0):
#    print("entered no is positive")
#elif(num<0):
#    print("entered no is negative")
#else:
#    print("entered no is zero")

#input 3 numbers and find the largest
# num1=int(input("Enter no1"))
# num2 = int(input("Enter no2"))
# num3=int(input("Enter no3"))
# if((num1>num2)&(num1>num3)):
#    print(num1,"is the largest no")
# elif((num2>num1) & (num2>num3)):
#    print(num2,"is the largest no")
# else:
#    print(num3,"is the largest no")

#enter the 2nd largest no


# num1=int(input("Enter no1"))
# num2 = int(input("Enter no2"))
# num3=int(input("Enter no3"))
# if((num1>num2) & (num1>num3)):
#     if(num2>num3):
#         print(num2,"is the 2nd largest")
#     else:
#         print(num3,"is the 2nd largest")
# elif((num2>num3) & (num2>num1)):
#     if(num1>num3):
#         print(num1,"is the 2nd largest")
#     else:
#         print(num3,"is the 2nd largest")
# else:
#     if(num1>num2):
#         print(num1,"is the 2nd greatest")
#     else:
#         print(num2,"is the 2nd greatest")

#read name of a student and enter 3 marks and assign to a variable,calculate total
#total>145 print a+
#total 140-145 print a
#total 135-140 print b+

id=input("Enter the name of student")
sub1=int(input("Enter the mark of subject 1"))
sub2=int(input("Enter the mark of subject 2"))
sub3=int(input("Enter the mark of subject 3"))
tot=sub1+sub2+sub3
print("Total marks obtained",tot)
if(tot>145):
    print(id,"-Your grade is A+")
elif((tot>140) & (tot<145)):
    print(id,"-Your grade is A")
elif((tot>135) & (tot<=140)):
    print(id,"-Your grade is B+")
else:
    print("Failed")
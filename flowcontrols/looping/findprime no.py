#to check prime no using flag
# num=int(input("Enter the no"))
# flag=0
# for i in range(2,num):
#     if(num%i==0):
#         print("NOT A PRIME")
#         break
# else:
#     print("It is a prime no ")

# find prime no in range 2-50(3,5,7,11.....47 etc)
lower=int(input("Enter the lower limit"))
upper=int(input("Enter the upper limit"))
flag=0
for i in range(lower,(upper+1)):
    for j in range(2,i):
        flag=0
        if(i%j==0):
            flag=1
            break
        else:
            pass
    if(flag==1):
        pass
    else:
        print(i)



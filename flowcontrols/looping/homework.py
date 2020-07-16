#find the sum of prime numbers between a range
lower=int(input("Enter the lower limit"))
upper=int(input("Enter the upper limit"))
sum=0
for i in range(lower,(upper+1)): #1
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
        else:
            pass
    if(flag==1):
        pass
    else:
        sum=sum+i

print(sum)
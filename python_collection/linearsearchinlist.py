# [4,6,8]=>[14,12,10]
# [3,4,8]=>[12,11,7]
lst=[1,2,3,4,5,6,7,8,9]
n=int(input("Enter the no to be searched"))
for i in lst:
    if(i==n):
        print("value present in",i,"th place")
        break
else:
    print("Value not found")
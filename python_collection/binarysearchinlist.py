#search using binary search
# lst=[10,12,9,15,13,19,20]
#
# lst.sort()
# lower=0
# flag=0
# upper=len(lst)-1
# e=int(input("Enter the value to be searched "))
# while(lower<=upper):
#     mid=(lower+upper)//2
#     if(e>lst[mid]):
#         lower=mid+1
#     elif(e==lst[mid]):
#         print("Element found")
#         flag=1
#         break
#
#     elif(e<lst[mid]):
#         upper=mid-1
# if flag==1:
#     pass
# else:
#     print("Element not found")
lst=[10,23,45,23,89,46,35,23,78]
lst.sort()
e=int(input("Enter the element to be searched"))
lower=0
flag=0
upper=len(lst)-1
while(lower<=upper):
    mid=(lower+upper)//2
    if(e>lst[mid]):
        lower=mid+1
    elif(e<lst[mid]):
        upper=mid-1
    elif(e==lst[mid]):
        print("Element found")
        flag=1
        break
if(flag==1):
    pass
else:
    print("Element not found")

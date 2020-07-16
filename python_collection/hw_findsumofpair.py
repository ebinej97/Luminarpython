#create a list and find the pair which gives the user input no as sum
lst=[]
pair=[]
for i in range(1,10):
    lst.append(i)
e=int(input("Enter the value"))
for i in lst:
    for j in lst:
        if(i<=j):
            if(i+j==e):
                if (i != j):
                    pair=[i,j]
                    print(pair)
                    break
if(len(pair)==2):
    pass
else:
    print("No Match")



#
# lst=[1,2,3,4,5]
# pair=[]
# flag=0
# e=int(input("Enter the value"))
# for i in lst:
#     for j in lst:
#         if(i<=j):
#             if(i+j==e):
#                 pair=[i,j]
#                 if(i!=j):
#                     print(pair)
#                     break
# if(len(pair)==2):
#     pass
# else:
#     print("No Match")




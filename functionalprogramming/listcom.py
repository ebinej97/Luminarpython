#
# lst=[1,2,3,4,5,6,7,8]
# sqlst=[(i*i) for i in lst]
# print(sqlst)

lst=[1,2,3]
lst2=[4,5,6]
#
#
# # for i in lst:
# #     for j in lst:
# #         print((i,j))
#
#
# pairs=[(i,j)for i in lst for j in lst2]
# print(pairs)
#
pairs2=[(i**j) for i in lst for j in lst2]
print(pairs2)
#
# #to select only even no
# evens=[i for i in lst if i%2==0]
# print(evens)

#map / filter
# map is used to apply to all values
# filter is used to apply to or filter out particular values


lst=[10,20,30,40,50]
  # def square(num1):
  #     return(num1**2)
sqlst=list(map(lambda num1:num1**2,lst))
print(sqlst)
cube=list(map(lambda num1:num1**3,lst))
print(cube)

#print even no in a lsit
lst=[10,11,12,13,14,15,16,17,18,19,20]

# def numcheck(num1):       lambda function
#     return(num1%2==0)

even=list(filter(lambda num1:num1%2==0,lst))
print(even)
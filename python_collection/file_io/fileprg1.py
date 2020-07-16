#read a file
f=open("C:/Users/ebins/PycharmProject/luminartech/python_collection/file_io/pythonbatch","r")
# for data in f:
#     print(data)
lst=[]
for name in f:
    lst.append(name.rstrip("\n"))
print(lst)

# f=open("C:/Users/ebins/PycharmProject/luminartech/python_collection/file_io/movies.csv","r")
# dict={}
# i=0
# for lines in f:
#     words=lines.rstrip("\n").split(",")
#     print(words)
#     year=words[2]
#     if(year not in dict):
#         dict[year]=1
#     else:
#         dict[year]+=1
#     i+=1
#     if(i==50):
#         break
# print(dict)


f=open("C:/Users/ebins/PycharmProject/luminartech/python_collection/file_io/movies.csv","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    year=words[2]
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
print(dict)


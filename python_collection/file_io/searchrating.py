#rating counter
f=open("C:/Users/ebins/PycharmProject/luminartech/python_collection/file_io/movies.csv","r")
dict={}
i=0
for lines in f:
    words=lines.rstrip("\n").split(",")
    print(words)
    rating=words[3]
    if rating not in dict:
        dict[rating]=1
    else:
        dict[rating]+=1
        i+=1
    if(i==50):
        break
for k,v in dict.items():
    print(k,"=>",v)
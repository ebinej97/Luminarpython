f=open("C:/Users/ebins/PycharmProject/luminartech/python_collection/file_io/data")
dict={}
for line in f:
    # print(line)
    words=(line.rstrip("\n").split(" "))
    print(words)
    for word in words:
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,"=>",v)
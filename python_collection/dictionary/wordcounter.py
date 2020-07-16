#count no of words in a string and store as dictionary
text="hai hello hai hello"
words=text.split(" ")
print(words)
dict={}
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
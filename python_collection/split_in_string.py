#split a string and remove duplicate words
data="this is a this is a random text to check to check"
words=data.split(" ")
print(words)
st=set(words)
print(st)
#text is "ABABA"
text=input("Enter the string")
chara=list(text)
print(chara)
dict={}
flag=0
for i in chara:
    if i not in dict:
        dict[i]=1
    else:
        print("The first reccuring character is ",i)
        flag=1
        break
if (flag==1):
    pass
else:
    print("No reccuring character")
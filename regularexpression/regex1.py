import re
# matcher=re.finditer("ab","ababababababababaghvhjgjhgbababnvcvcvcvvcba")
# count=0
# for match in matcher:
#     print(match.start())
#     print(match.group())
#     count+=1
# print(count)

count=0
# x='[abc]'  #check either a b or c
# x='[a-z]'  #check from a to z small letter
# x='[0-9]'   #check from 0 to 9
# x='[a-zA-Z0-9]' #check a to z,A to Z ,check for 0 to 9
# x='[^a-z]'  #check for all characters except a to z
# x='[^0-9]'  #check for all characters except 0 to 9
x='[^a-zA-Z0-9]'
matcher=re.finditer(x,"ab7k_@9Z")
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
# print(count)

#predefined characters
# '\s' =>check for space
# '\d' =>check for digit 0 to 9
# '\D' =>check for ^0 to 9
#'\w' => check for [a-zA-Z0-9]
#'\W' => check for [^a-zA-Z0-9]


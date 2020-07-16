#quantifiers
import re
#x="a+" #check for single and combination of 'a'
#x="a*" #check for single/comb of 'a' and also for position where'a' is not present

# x="a?"  #check for single occurance of a
# x='a{2}' #check for combination of 2 'a'
# x='a{2,3}' #check for combination of minimum 2 no of 'a' and max 3 no of 'a'
# x='^a'  #check for whether the pattern is starting with a or not
x='&$' #check whether the string ends with '&'
matcher=re.finditer(x,"aaaaabbbbaaaababbaaababbaa&")

for match in matcher:
    print(match.start())
    print(match.group())
####dictionary
# person={"name":"ajay","age":25,"gender":"male"}
# print(person["name"])
# print(person)

#sample prg for dictionary
emp={"name":"ebin","salary":25000,"designation":"team lead","id":234}
print(emp["designation"])
for k,v in emp.items():
    print(k,v)
emp["exp"]=2
print(emp)
emp["salary"]+=50000
print(emp)
print("name" in emp)

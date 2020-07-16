class product:
    def __init__(self,id,name,category,price):
        self.id=id
        self.name=name
        self.category=category
        self.price=price

    def __str__(self):
        return self.name
lst=[]
ob=lst.append(product(100,"lux","soap",20))
ob=lst.append(product(102,"colgate","paste",50))
ob=lst.append(product(103,"nike","shoe",1000))
# for item in lst:
#     print(item)



# def con(name):
#     return name.upper()
# print(con("nike"))
# a=lambda name:name.upper()
namelst=list(map(lambda product:product.name.upper(),lst))
print(namelst)
price=list(filter(lambda product:product.price>50,lst))
for value in price:
    print(value)

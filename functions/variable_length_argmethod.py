#variable length argument

#sample prg
# def add(**kwargs):          #will recieve any no of args and act as a dict
#     total=0
#     print(kwargs)
#     for k,v in kwargs.items():
#         total=total+v
#     print(total)
#
# add(num1=10,num2=20,num3=30,num4=40)

def add(**kwargs):
    sum=0
    print(kwargs)
    for k,v in kwargs.items():
        sum=sum+v
    print(sum)
add(n=1,m=2,l=3,w=4,r=5)
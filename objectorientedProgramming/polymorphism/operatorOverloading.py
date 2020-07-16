class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return(self.pages+other.pages)
    def __sub__(self,other):
        return(self.pages-other.pages)

b=book(100)
c=book(200)
print(b+c)
print(b-c)
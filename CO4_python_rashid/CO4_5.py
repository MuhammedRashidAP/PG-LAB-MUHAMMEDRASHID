class publisher:
    def getbook(self):
        self.title=input("title :")
        self.author=input("author :")
class python(publisher):
    def getdetails(self):
        self.price=int(input("price :"))
        self.nopages=int(input("no of pages :"))
    def display(self):
        print("title of the book is :",self.title)
        print("author of the book is :",self.author)
        print("price is: ",self.price)
        print("number of pages :",self.nopages)


a=python()
a.getbook()
a.getdetails()
a.display()

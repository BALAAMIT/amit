class library:
    def __init__(self):
        self.noBooks = 0
        self.Books = []
    
    def addbook(self):
        Book = input("Enter books...")
        self.Books.append(Book)
        self.noBooks = len(self.Books)

    def showinfo(self):
        print(f"the library has {self.noBooks} books name is {self.Books} ")
l1 = library
l1.addbook()
l1.showinfo()

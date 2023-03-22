class parsan:
    def __init__(self,n,o) -> None:
        print("hey i am i parson")
        self.name = n
        self.occ = o

    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = parsan("harry","developer")
a.info()
# b = parsan()
class Animal:
    def __init__(self,name,species):
        self.name= name
        self.species = species

    def show_Details(self):
        print(f"Name is {self.name}")
        print(f"Species is {self.species}")



class dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="dog")
        self.breed = breed
    def show_Details(self):
        Animal.show_Details(self)
        print(f"breed is: {self.breed}")

class GoldenRetriever(dog):
    def __init__(self, name,color) -> None:
        dog.__init__(self,name, breed="Golden Retriever")
        self.color = color
    def show_Details(self):
        dog.show_Details(self)
        print(f"color is :{self.color}")


o = GoldenRetriever("Tommy","black",)
o.show_Details()
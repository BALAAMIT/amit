class Employee:
    compny = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.compny} ")
    @classmethod
    def changeCompany(cls,newCompany):
        cls.compny = newCompany

e1 = Employee()
e1.name = "amit"
e1.show()
e1.changeCompany("Tasla")
e1.show()
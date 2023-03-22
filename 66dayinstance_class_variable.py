class Employee:
    compny_name= "apple"
    def __init__(self,name, id):
        self.name = name
        self.raise_amount = 0.02
    def showDetails(self):
        print(f"The name of Employee: {self.name} and iraise amount {self.raise_amount}and compny name{self.compny_name  }")
class programmer(Employee):
    def showlangauge(self):
        print("The defult langauge is python ")
#Employee.showDetails(e)


e1= Employee("rohan das ",400)
e1.raise_amount=0.4
e1.compny_name="apple india"
e1.showDetails()

e2= Employee("rohan das ",400)
e2.showDetails()
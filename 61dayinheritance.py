class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee: {self.name} and id is {self.id}")
class programmer(Employee):
    def showlangauge(self):
        print("The defult langauge is python ")
e = Employee("rohan das ",400)
e.showDetails()
e2 = programmer("amit bala",2555)
e2.showlangauge()
e2.showDetails()
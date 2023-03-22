class Employee:
    def __init__(self,Name,salary) -> None:
        self.name =Name
        self.salary= salary

    @classmethod
    def formStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

string = "harry-12000"

e1=Employee("amit",10000)
print(e1.name)
print(e1.salary)

e2 = Employee.formStr(string)
print(e2.name)
print(e2.salary)
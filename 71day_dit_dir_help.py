#dir
x=[1,2,3]
print(dir(x))
print(x.__add__)


#dict
class person:
    def __init__(self,name,salary) -> None:
        self.name=name
        self.salary=salary
        self.ver = 1
p = person("join",30)
print(p.__dict__)

#help method
print(help(person))
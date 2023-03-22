class Employee:
    def __init__(self,name):
        self.name = name
    def __len__(self):
        i = 0
        for c in self.name:
            i +=1
        return i
    def __str__(self):
        return f"The Employee name is {self.name} "
    def __repr__(self):
        return f"Employee('{self.mane}')"
    def __call__(self):
        return f" hey {self.name} i am good"
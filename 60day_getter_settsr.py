class myClass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"value is {self._value}")

@property
def _value(self):
    return 10*self._value

obj = myClass(10)
print(obj._value)
obj.show()
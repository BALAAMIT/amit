class shape:
    def __init__(self,x,y) -> None:
        self.x= x
        self.y = y
    def area(self):
        return self.x*self.y
class circle(shape):
    def __init__(self,redius):
        self.redius=redius
        super().__init__(redius,redius)
    # def area(self):
    #     return 3.14*self.redius
        #second methad overloding
        
    def area(self):
         return 3.14*super().area()





rec = shape(3,5)
print(rec.area())
c =circle(5)
print(c.area())
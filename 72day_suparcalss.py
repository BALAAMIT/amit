class prentClass:

    def prent_Method(self):
        print("this is prent method class")
class childClasss(prentClass):
    def child_Method(self):
       print("this is a child class method")
       super().prent_Method()
    def prent_Method(self):
        print("Amit")
child_ob=childClasss()
child_ob.child_Method()
child_ob.prent_Method()



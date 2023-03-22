class person :
    name = "amit"
    occuption = "sw"
    networth  = 10
    def info(self):
        print(f"{self.name}is a {self.occuption}")

a = person()
b = person()
b.name = "subham"
b.occuption = "ac"
# print(a.name ,a.occuption)
b.info()
a.info()
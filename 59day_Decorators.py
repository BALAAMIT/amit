def greet(fx):
    def mfx(*args,**kwargs):
        print("good mornig")
        fx(*args,**kwargs)
        print("thanks for using this functoin ")
    return mfx
@greet
def hello():
    print("hello wold")
@greet
def addt(a,b):
    print(a+b)

hello()
addt(1,2)
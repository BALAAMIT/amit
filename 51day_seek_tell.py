# with open("file.txt",'r')as f:
#     print(type(f))
#     f.seek(15)
#     print(f.tell())
#     data= f.read(5)
#     print(data)
with open("sampal.txt","w")as f:
    f.write("hello world!")
    f.truncate(5)
with open("sampal.txt","r")as f:
    print(f.read())

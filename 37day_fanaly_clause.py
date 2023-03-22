# try:
#     l = [1,2,3]
#     i = int(input("Enter number index..:"))
#     print(l[i])
# except:
#     print("some error occurred")
# finally:
#     print("i always executed")

def fun1():
    try:
        l = [1,2,3]
        i = int(input("Enter number index..:"))
        print(l[i])
    except:
       return ("some error occurred")
    finally:
       return ("i always executed")
if __name__ == "__main__":
    x=fun1()
    print(x)



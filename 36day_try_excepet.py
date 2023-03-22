a = input("Enter The number..")
print(f"multiplication table of {a} is :")
try:
     for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*(i)}")
except Exception as e:
    print("Invalid input ",e)
print("some code ")
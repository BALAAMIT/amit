# a = True
# print(a:=False)


# num = [1,2,3,4,5,6]
# while (n:=len(num))>0:
#     print(num.pop())
# print(num)
#NOTE sempal Ex
# foods = list()
# while True:
#     food = input("what food do you like?:")
#     if food == "Quit":
#         break
#     foods.append(food)
# print(foods)
#NOTE walrus ex
foods = list()
while (food :=input("what food do you like?:")) !="Quit":
    foods.append(food)
t = (1,2,5,6,8,7,4,9,4,)
l1 = list(t)
l1.append(25) # tupale ko change karne ke liye use list me convert karna padta hai
t = tuple(l1)
# print(t)
# print(l1)

r = t.count(4)
r2 = t.index(4,3,8)# 3,8,secing ka kam kar raha hai
print(r2)

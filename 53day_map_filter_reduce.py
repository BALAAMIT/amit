from functools import reduce 
#   MAP
def cube(x):
    return x*x*x
l = [1,2,4,6,4,3]
# newl = []
# for i in l:
#     newl.append(cube(i))  normal methad
# print(newl)
newl= list(map(cube,l))
print(newl)
#   FILTER
def filter_f(a):
    return a>2
newll = list(filter(filter_f,l))
print(newll)
# MAP 2 methad
newll = list(map(lambda x:x*x*x,l))
print(newll)
number = [1,2,5,8,7,98]
newl2 = reduce(lambda x ,y:x+y,number)
print(newl2)
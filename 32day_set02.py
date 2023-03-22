# s = {1,3,35,57,}
# s2 = {2,6,9,5}
# # print(s.union(s2))
# s.update(s2)
# print(s)
city = {"satna","panna","chatrarpur",'damoh','jablpur','katni','sagar','bhopal','indor'}
city2= {'nagpur','chandarpur','kamleshwar','mumbai','chenai','shirdi',"bhopal7"}
# city.intersection_update(city2)
# city3 = city.symmetric_difference(city2)
# city3 = city.difference(city2)
# city3 = city.isdisjoint(city2)
city3 = {"satna","panna","jablpur"}
print(city.issuperset(city3))
print(city3.issubset(city))
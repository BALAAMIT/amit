dic = {"spoon":"object"}
info = {"name":"amit","age":23,"add":"nagpur"}
# print(info["age2"])
# print(info.get("age3"))

# print(info.keys())
for key  in info.keys():
    print(f" the value corresponding to the key {key} is {info[key]}")

# print(info.items())
for key , value in info.items():
    print(f" the value corresponding to the key {key} is {value}")

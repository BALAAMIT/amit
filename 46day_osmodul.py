import os as o
if(not o .path.exists("Data")):
    o.mkdir("data")

for i in range(1,101):
    o.mkdir(f"Data?day{i}")

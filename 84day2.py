import time
# print(4)
# time.sleep(10)
# print("thi print after 10 sec")
t=time.localtime()
formatted_time = time.strftime("%Y-%m-%d-%H-%M-%S",t)
print(formatted_time)
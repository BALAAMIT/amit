def factorl(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorl(n-1)
print(factorl(3))
print(factorl(5))
print(factorl(0))

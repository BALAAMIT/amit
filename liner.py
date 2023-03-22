def linear_searchlist(list1,n,key):
    for  i in range (0,n):
        if(list1[1]==key):
            return 1

    return -1
if __name__== "__main__":
    list1 = [1,3,5,4,7,9]
    key = int(input("Enter interjar num."))
    n = len(list1)
    res = linear_searchlist(list1,n,key)
    if(res == -1):
        print("Element Not Found")
    else:
        print("Elemet fount at index : ",res)
linear_searchlist(list1,n,res)


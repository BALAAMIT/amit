def power_f(n):
    if n == 0 :
        return 1
    else:
        
        # for i in range(n):
        e = 2*power_f(n-1)
            # e.append(m)
        print(e)

        
        # if e ==s:
        #     print(True)
        # else:
        #     print(False)
# x= int(input("Enter  NUM...-:"))
# s= int(input("Enter surch NUM...-:"))

power_f(7)
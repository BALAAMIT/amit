def minimumcoust(cost,n):
    dp1 = 0 
    dp2 = 0
    dp = 0 
    for i in range(n):
        dp = cost[i]+min(dp1,dp2)
        dp2 = dp1
        dp1 = dp
    return min(dp1,dp2)

if __name__== "__main__":
    a = [2,5,3,1,7,2,4]
    n =len(a)

print(minimumcoust(a,n))
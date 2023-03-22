def fib(n):
    # n = int(input("Enter Number>> .. :"))
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def countWays(s):
    return fib(s + 1)
print(countWays(6))
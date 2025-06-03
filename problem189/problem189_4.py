# 159   ########## dbt

n, m = map(int, input().split())

def factorial(a):
    p = 1
    for i in range(a, 0 , -1):
        p *= i
    return p

def combo(b, num):
    ans = factorial(b) // (factorial(num) * factorial(b - num))
    return ans

print(combo(n, 2) + combo(m, 2))
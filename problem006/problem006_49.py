def f(a,b):
    if (b == 0): return a
    a = a * 1.05
    if (a%1000 != 0): a = a - a%1000 + 1000
    return f(a,b-1)
print int(f(100000,input()))
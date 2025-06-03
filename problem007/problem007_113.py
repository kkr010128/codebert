n = int(input())

dict = {0:1,1:1}

def fib(n):
    if n in dict.keys():
        return dict[n]
    else:
        dict[n] = fib(n-1) + fib(n-2)
        return dict[n]

print(fib(n))

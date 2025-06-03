def Fibonacci(n):
    if n == 0 or n == 1:
        dic[n] = 1
    if n in dic.keys():
        return dic[n]
    dic[n] = Fibonacci(n-1) + Fibonacci(n-2)
    return dic[n]

a = int(input())
dic ={}
print(Fibonacci(a))

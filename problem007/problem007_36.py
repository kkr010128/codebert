def fib(n):
    if n ==0 or n == 1:
        return 1
    l = [0] * (n+1)
    l[0] = 1
    l[1] = 1

    for i in range(2,n+1):
        l[i] = l[i-2] + l[i-1]
    return l[i]

print(fib(int(input())))


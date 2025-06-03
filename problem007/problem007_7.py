F = [0 for i in range(50)]
F[0] = 1
F[1] = 1

def fib(n) :
    if n == 0 or n == 1:
        F[n] = 1
        return F[n]
    else:
        if F[n] == 0:
            F[n] = fib(n-1) + fib(n-2)
            return F[n]
        else:
            return F[n]
n = int(input())
print(fib(n))

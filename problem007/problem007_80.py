N = int(input())

memolist = [-1]*(N+1)
def fib(x):
    if memolist[x] == -1:
        if x == 0 or x == 1:
            memolist[x] = 1
        else:
            memolist[x] = fib(x - 1) + fib(x - 2)
    return memolist[x]

print(fib(N))

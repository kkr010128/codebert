def fib(n):
    F = {0:1, 1:1}
    def fibonacci(n):
        ans = F.get(n,-1)
        if ans > 0: return ans
        F[n] = fibonacci(n-1) + fibonacci(n-2)
        return F[n]
    return fibonacci(n)
        
if __name__=='__main__':
    print(fib(int(input())))
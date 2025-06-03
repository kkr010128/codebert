def fibonacci(F,n):
    F[0] = 1
    F[1] = 1
    for i in range(2,n+1,1):
        F[i] = F[i-1] + F[i-2]
    return F[n]

def main():
    n = int(input())
    F  = [0]*(n+1)
    ans = fibonacci(F,n)
    return ans

print(main())


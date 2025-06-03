N = int(input())

memo = [-1]*500

def fibo(x):
    if memo[x] != -1:
        return memo[x]
    
    if x == 0 or x == 1:
        ans=1
        memo[x] = ans
        return ans
    
    ans = fibo(x-1) + fibo(x-2)
    memo[x] = ans
    return ans

print(fibo(N))

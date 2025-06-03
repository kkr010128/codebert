def solve():
    N = int(input())
    
    if N % 2 != 0:
        return 0
    else:
        ans = 0
        N //= 10
        while N > 0:
            ans += N
            N //= 5
        return ans
    
print(solve())
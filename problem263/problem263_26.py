import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ans = 0
MOD = 10**9+7

for i in range(63):
    one, zero = 0, 0
    
    for Aj in A:
        if (Aj>>i)&1:
            one += 1
        else:
            zero += 1
    
    ans += 2**i*one*zero
    ans %= MOD

print(ans)
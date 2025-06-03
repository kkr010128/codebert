n = int(input())
A = list(map(int, input().split()))

mod = 10**9+7

A = [a+1 for a in A]
C = [0]*(n+1)
C[0] = 3
ans = 1
for a in A:
    if C[a-1] < C[a]:
        print(0)
        exit()
    else:
        ans *= C[a-1]-C[a]
        ans %= mod
        C[a] += 1
print(ans)
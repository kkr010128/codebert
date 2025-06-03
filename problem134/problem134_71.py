N = int(input())
A = list(map(int, input().split()))
ans = 1
P = 10**18

for i in range(N):
    ans *= A[i]
    if ans > P:
        ans = -1
        break

ans = 0 if any([a==0 for a in A]) else ans
print(ans)
N = int(input())
A = list(map(int,input().split()))
S = sum(A)
T = 0
ans = float("inf")
for e in A:
    T += e
    ans = min(ans,abs(T-(S-T)))
print(ans)

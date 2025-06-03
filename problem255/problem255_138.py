N = int(input())
S, T = input().split()
ans = ""

for p in range(N):
    ans += S[p]
    ans += T[p]

print(ans)
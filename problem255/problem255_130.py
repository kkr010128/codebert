N = int(input())
S, T = (x for x in input().split())
ans = ''
for i in range(N):
    ans += (S[i] + T[i])

print(ans)
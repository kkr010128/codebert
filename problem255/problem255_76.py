
N = int(input())
S, T = map(str, input().split())

ans = ""
for s, t in zip(S, T):
    ans += s + t

print(ans)

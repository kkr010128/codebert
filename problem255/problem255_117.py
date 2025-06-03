n = int(input())
s, t = map(str, input().split())
ans = ''
for a, b in zip(s, t):
    ans += a+b
print(ans)
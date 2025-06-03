n = int(input())
s, t = input().split()

ans = ""
for x in range(n):
    ans = ans + s[x]
    ans = ans + t[x]
print(ans)
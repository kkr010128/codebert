n = int(input())
s = []
for _ in range(n):
    s.append(input())

s.sort()

ans = n
for i in range(n-1):
    if s[i] == s[i+1]:
        ans -= 1

print(ans)
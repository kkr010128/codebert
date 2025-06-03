n = int(input())
s,t = map(str, input().split())
res = str()
for i in range(n):
    res += s[i]
    res += t[i]
print(res)
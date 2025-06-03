n = int(input())
s, t = map(str, input().split())  

s = list(s)
t = list(t)

c = ""
for i in range(n):
  c += s[i]+t[i]

print(c)
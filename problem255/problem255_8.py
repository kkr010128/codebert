n = int(input())
s,t = input().split()
res = ""
for i in range(0,n):
  res += s[i]
  res += t[i]
print(res)
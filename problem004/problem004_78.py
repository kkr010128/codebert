n = int(input())
s = ""
for i in range(n):
  l = list(map(lambda x:x*x,map(int, input().split())))
  l.sort()
  if l[0] + l[1] == l[2]:
      s += "YES\n"
  else:
      s += "NO\n"

print(s,end="")
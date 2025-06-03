import sys

n = int(input())
l = sys.stdin.readlines()
s = ""
for i in l:
  x, y, z = sorted(map(lambda x:x*x,map(int, i.split())))
  if x + y == z:
      s += "YES\n"
  else:
      s += "NO\n"

print(s,end="")
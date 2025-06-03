input()
a=1
d=1000000000000000000
for i in input().split():
  a=min(a*int(i),d+1)
print([a,-1][a>d])
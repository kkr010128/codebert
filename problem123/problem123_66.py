n,*a = map(int,open(0).read().split())
all = 0
for i in a:
  all^=i
print(*[all^i for i in a])
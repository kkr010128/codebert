n,*a=map(int,open(0).read().split())
sa = sum(a)
ha = sa/2
x = 0
for i in range(n):
  x+=a[i]
  if x>=ha:
    break
y = sa-x
print(min(abs(x-y),abs((x-a[i])-(y+a[i]))))
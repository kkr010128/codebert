a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = 0
for i in range(a[0]):
  if b[i] >= a[1]:
    c += 1
print(c)
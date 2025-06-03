n = int(input())
x = list(map(int,input().split()))
k = []
def kyori(p):
  m = 0
  for i in range(n):
    m += (p-x[i])**2
  return m
for i in range(1,101):
  k.append(kyori(i))

print(min(k))
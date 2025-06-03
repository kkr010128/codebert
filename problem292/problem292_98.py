a = int(input())
b = list(map(int, input().split()))
c = 0
for i in range(a-1):
  for j in range(1,a-i):
    c += b[i]*b[i+j]
print(c)


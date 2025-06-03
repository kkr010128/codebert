import math
n,d = map(int,input().split())
#l = list(map(int, input().split()))
x = [0] * n
y = [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())
#print(n,d,x,y)

count = 0
for i in range(n):
  #print(math.sqrt(x[i]**2 + y[i]**2))
  if math.sqrt(x[i]**2 + y[i]**2)<=d:
    count += 1
print(count)
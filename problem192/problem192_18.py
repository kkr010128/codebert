n = int(input())
lst = list(map(int,input().split()))

num = [0] * n
for i in lst:
  num[i-1] += 1
  
total = 0
for i in range(n):
  m = num[i]
  total += m*(m-1)//2

for k in range(n):
  
  s = num[lst[k]-1]
  t = total + 1- s
  
  print(t)  
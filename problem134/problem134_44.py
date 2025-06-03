n = int(input())
a = list(map(int,input().split()))
a.sort()
t = 1
 
for i in range(len(a)):
  t *= a[i]
  if t > 10**18:
    break
 
if t > 10**18 :
  print("-1")
else:
  print(str(t))
n = int(input())
a = list(map(int,input().split()))
a = sorted(a)
#print(a)
if a[0]==0 :
  print(0)
  exit()

res = 1

lim = 10**18

for i in(a):
  res *= i
  if res > lim :
    print(-1)
    exit()
  
print(res)
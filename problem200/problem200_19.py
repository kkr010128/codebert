a,b,m = input().split()

a = list(map(int,input().split()))
b = list(map(int,input().split()))
xyc =[]
for i in range(int(m)):
  xyc.append(input())
  
min = min(a) + min(b)
for i in xyc:
  x,y,c = map(int, i.split())
  if min > a[x-1] + b[y-1] - c :
    min = a[x-1] + b[y-1] - c
print(min)

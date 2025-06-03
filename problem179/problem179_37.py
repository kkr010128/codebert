n,m = input().split()
n = int(n)
m = int(m)
arr = list(map(int,input().split()))
minn = sum(arr)*(1/(4*m))
t = 0
for i in arr:
  if i >= minn:
    t += 1
#print(t)
if t >= m:
  print("Yes")
else:
  print("No")
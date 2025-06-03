n,m =map(int,input().split())
a = list(map(int,input().split()))
cnt=0;s=0;
for i in range(n):
  s += a[i]

for i in a:
  if i *4*m>=s: cnt +=1
  if cnt >= m:
    print("Yes")
    break
  
else:
  print("No")
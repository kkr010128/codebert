a,b=map(int,input().split())
for i in range(100001):
  if int(i*0.08) == a and int(i*0.1) == b:
    print(i)
    break
else:
  print(-1)
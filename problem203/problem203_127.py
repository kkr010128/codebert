a,b=map(int,input().split())
c=b*10
for i in range(c,c+10):
  if int(i*0.08)==a:
    print(i)
    exit()

print(-1)
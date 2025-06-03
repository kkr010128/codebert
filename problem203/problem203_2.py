a,b=map(int,input().split())
ans=(b-a)/0.02

for i in range(1,1000001):
  aans=0.08*i
  bans=0.10*i
  if int(aans)==a and int(bans)==b:
    print(i)
    exit()

print("-1")
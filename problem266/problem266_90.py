x=int(input())
if x>=2100:
  print(1)
  exit()

ans=[0]*2100
for a in range(22):
  for b in range(22):
    for c in range(22):
      for d in range(22):
        for e in range(22):
          for f in range(21):
            y=a*100+b*101+c*102+d*103+e*104+f*105
            if y<=2099:
              ans[y]=1
            
print(ans[x])
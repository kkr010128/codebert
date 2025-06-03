n,m=map(int,input().split())
aa=[[] for i in range(n)]
for x in range(m):
  a,b=input().split()
  d=int(a)-1
  aa[d].append(b)
  
ans_ac=0
ans_wa=0
for y in range(n):
  ans1=0
  ans2=0
  for z in range(len(aa[y])):
    if aa[y][z]=='WA':
      ans1+=1
    else:
      ans2+=1
      break
  if ans2==1:
    ans_wa+=ans1
    ans_ac+=1
    
print(str(ans_ac)+' '+str(ans_wa))
  

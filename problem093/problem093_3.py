n,k=map(int,input().split())
p=list(map(int,input().split()))
c=list(map(int,input().split()))
ans=[]
for i in range(n):
  ct=0
  score=0
  s=[]
  pos=i
  while ct<k:
    ct+=1
    pos=p[pos]-1
    score+=c[pos]
    s.append(score)
    if pos==i:
      break
  if s[-1]<0:
    ans.append(max(s))
  elif pos!=i:
    ans.append(max(s))
  elif k%len(s)==0:
    ans.append(s[-1]*(k//len(s)-1)+max(s))
  else:
    ans.append(max(s[-1]*(k//len(s)-1)+max(s),s[-1]*(k//len(s))+max(s[0:k%len(s)])))
print(max(ans))
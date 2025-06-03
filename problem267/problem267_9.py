N=int(input())
S=input()
ans=0
for i in range(10):
  for j in range(10):
    for k in range(10):
      p,q,r=str(i),str(j),str(k)
      if p in S:
        x=S.index(p)
        S_=S[x+1:]
        if q in S_:
          y=S_.index(q)
          S__=S_[y+1:]
          if r in S__:
            ans+=1
print(ans)
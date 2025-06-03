h,w,k=map(int,input().split())
cho=[]
for _ in range(h):
    a=list(input())
    for f in range(w):
      a[f]=int(a[f])
    cho.append(a)

ans=1000000000009

for i in range(2**(h-1)):
    cut=0
    cut_n=[]
    b=[]
    for j in range(h-1):
        if (i>>j)&1:
            cut_n.append(j+1)
            cut+=1
    if len(cut_n)==0:
        ok=1
        dp=0
        for i in range(w):
            wa=0
            for j in range(h):
                wa+=cho[j][i]

            if dp+wa>k:
                cut+=1
                dp=wa
            else:
              dp+=wa

            if wa>k:
                ok+=1
                break
            
        if ok==1:
          ans=min(ans,cut)

    else:
        st=0
        for t in range(len(cut_n)):
            if t==len(cut_n)-1:
                b.append(cut_n[t]-st)
                b.append(h-cut_n[t])
            else:
              b.append(cut_n[t]-st)
              st=cut_n[t]
        
        dp=[0 for _ in range(len(b))]
        ok=1
        for y in range(w):
            for g in dp:
                if g>k:
                    ok+=1
                    break
            st=0
            ch=0
            c=[]
            for e in range(len(b)):
              p=b[e]
              temp=0
              for q in range(p):
                  temp+=cho[st+q][y]
                    
                  dp[e]+=cho[st+q][y]

              c.append(temp)
                
              st+=p

            for g in dp:
                if g>k:
                    ch+=1

            if ch!=0:
                cut+=1
                dp=c

            
            for last in c:
                  if last>k:
                      ok+=1

        
        if ok==1:
            ans=min(ans,cut)

print(ans)



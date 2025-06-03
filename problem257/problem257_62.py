N=int(input())
A=list(map(int,input().split()))
ans=[0]

cnt=0
hit=0
while cnt<N:
  if ans[hit]+1==A[cnt]:
    hit+=1
    ans.append(hit)
  cnt+=1
print(N-len(ans[1:]) if len(ans)>1 else -1)
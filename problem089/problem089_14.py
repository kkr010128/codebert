H,W,M=map(int,input().split())
L=[]
bh=[0]*(H+1)
bw=[0]*(W+1)
for _ in range(M):
    h,w=map(int,input().split())
    L.append((h,w))
    bh[h]+=1
    bw[w]+=1
p,q=max(bh),max(bw)
num=len(list(filter(p.__eq__, bh)))*len(list(filter(q.__eq__,bw)))
num-=len(list(filter(lambda x: bh[x[0]]==p and bw[x[1]]==q, L)))
ans=p+q-1
if num>0:
    ans+=1
print(ans)
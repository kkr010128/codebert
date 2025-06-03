n,k,c=map(int,input().split())
s=input()
l=len(s)
cand=[]
for i in range(l):
    if s[i]=='o':
        cand.append(i+1)
cnt1=[0]*(n+c+2)
cnt2=[0]*(n+c+2)        

for i in range(l):
    if s[i]=='o':
        cnt1[i+1]=max(cnt1[i],cnt1[i-c]+1)
    else:
        cnt1[i+1]=cnt1[i]
for i in range(l-1,-1,-1):
    if s[i]=='o':
        cnt2[i+1]=max(cnt2[i+2],cnt2[i+c+2]+1)
    else:
        cnt2[i+1]=cnt2[i+2]
ans=[]
for i in range(len(cand)):##嘘に見える
    tmp=cand[i]
    if cnt1[tmp-1]+cnt2[tmp+1]<k:
        print(tmp)

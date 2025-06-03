def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

N=II()
A=LI()
cnt=[0]*((10**6)+1)
for elem in A:
  cnt[elem]+=1
unique=[]
for i in range((10**6)+1):
  if cnt[i]==1:
    unique.append(i)
cnt=[0]*((10**6)+1)
A=list(set(A))
for elem in A:
  for m in range(elem*2,10**6+1,elem):
    cnt[m]=1
ans=0
for i in unique:
  if cnt[i]==0:
    ans+=1
print(ans)  
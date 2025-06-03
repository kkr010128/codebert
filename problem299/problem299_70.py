n=int(input())
l=list(map(int,input().split()))
la=[0]*n
for i in range(n):
  la[l[i]-1]=i+1
ans=[str(j) for j in la]
ans=" ".join(ans)
print(ans)
n=int(input())

p=10**9+7

A=list(map(int,input().split()))

binA=[]
for i in range(n):
  binA.append(format(A[i],"060b"))


lis=[0 for i in range(60)]

for binAi in binA:
  for j in range(60):
    lis[j]+=int(binAi[j])

binary=[0 for i in range(60)]

for i in range(n):
  for j in range(60):
    if binA[i][j]=="0":
      binary[j]+=lis[j]
    else:
      binary[j]+=n-lis[j]


binary[58]+=binary[59]//2
binary[59]=0


explis=[1]

for i in range(60):
  explis.append((explis[i]*2)%p)

ans=0
for i in range(59):
  ans=(ans+binary[i]*explis[58-i])%p

print(ans)


  

S=input()
k=int(input())
x=1
L=[]
for i in range(len(S)-1):
  if S[i]==S[i+1]:
    x+=1
  else:
    L.append(x)
    x=1
L.append(x)
s=sum([l//2 for l in L])
if S[0]!=S[-1]:
  print(s*k)
else:
  if len(L)>1:
    L[0]+=L[-1]
    print(s+sum([l//2 for l in L[:-1]])*(k-1))
  else:
    print(L[0]*k//2)
N=int(input())
S=input()
L=len(S)
Alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans=''
for i in range(L):
  k=Alph.index(S[i])
  ans+=Alph[(k+N)%26]
print(ans)
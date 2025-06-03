import sys
input=lambda: sys.stdin.readline().rstrip()
S=input()
n=len(S)
D=[0]*2019
T=[0]*(n+1)
T[0]=1
for i in range(n):
  T[i+1]=(T[i]*10)%2019

cur=0
keta=0
ans=0
D[0]+=1
for s in S[::-1]:
  cur=(cur+int(s)*T[keta])%2019
  ans+=D[cur]
  D[cur]+=1
  keta+=1
print(ans)
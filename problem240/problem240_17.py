N,M=list(map(int, input().split()))
P=[0]*M
S=[0]*M
for i in range(M):
    P[i],S[i]=list(input().split())
    P[i]=int(P[i])

flagac=[False]*N
pnlt=[0]*N
for i in range(M):
    p=P[i]-1
    s=S[i]
    if s=='AC':
        flagac[p]=True
    else:
        pnlt[p]+=(flagac[p]+1)%2
# print(flagac)
# print(pnlt)

ctac=0
ctwa=0
for i in range(N):
    if flagac[i]:
        ctac+=1
        ctwa+=pnlt[i]
print(ctac, ctwa)
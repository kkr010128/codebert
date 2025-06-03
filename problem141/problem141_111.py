N=int(input())

L=list(map(int,input().split()))

M=[0 for i in range(N+1)]
M[0]=1
if N==0:
    if L[0]==1:
        print(1)
        exit()
    else:
        print(-1)
        exit()
if L[0]==1:
    print(-1)
    exit()

for i in range(1,N+1):
    M[i]=M[i-1]*2-L[i]
    if M[i]<0:
        print(-1)
        exit()
#print(L)
#print(M)

M[-1]=0
for i in range(1,N+1):
    if M[-1-i]<(M[-i]+L[-i]+1)//2:
        print(-1)
        exit()
    elif (M[-i]+L[-i])>=M[-1-i] and M[-1-i]>=(M[-i]+L[-i]+1)//2:
        continue
    else:
        M[-1-i]=(M[-i]+L[-i])
#print(L)
#print(M)
print(sum(L)+sum(M))
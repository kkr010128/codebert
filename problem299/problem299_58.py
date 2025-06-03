N=int(input())
L=list(map(int,input().split()))
S=[0]*N
c=1
for i in L:
    S[i-1]=c
    c+=1
for i in range(N):
    print(S[i],end=' ')
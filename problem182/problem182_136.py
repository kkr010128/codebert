N,K,C=map(int, input().split())
S=input()

L=[0]*N
R=[0]*N
c=1
last=-C-1
for i in range(N):
    if i-last>C and S[i]!='x' and c<=K:
        L[i]=c
        c+=1
        last=i
c=K
last=N+C
for i in range(N-1,-1,-1):
    if last-i>C and S[i]!='x' and c>=1:
        R[i]=c
        c-=1
        last=i
for i in range(N):
    if 0<L[i]==R[i]: print(i+1)

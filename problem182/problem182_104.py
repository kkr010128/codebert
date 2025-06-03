N,K,C=list(map(int,input().split()))
S=input()
R=[]
L=[]

i=0
while i<N:
    if S[i]=="o":
        R.append(i)
        i+=C+1
    else:
        i+=1
i=N-1
while i>=0:
    if S[i]=="o":
        L.append(i)
        i-=(C+1)
    else:
        i-=1
R=R[:K+1]
L=L[:K+1]
L.reverse()
for i in range(K):
    if R[i]==L[i]:
        print(str(R[i]+1),end=" ")

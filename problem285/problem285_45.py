S=input()
N=len(S)+1

A=[0]*N
B=[0]*N

for k in range(N-1):
    if S[k]=="<":
        A[k+1]=A[k]+1

for k in range((N-1)-1,-1,-1):
    if S[k]==">":
        B[k]=B[k+1]+1
        
print(sum(map(lambda x:max(A[x],B[x]),range(N))))

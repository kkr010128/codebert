N=int(input())
C=input()

W=0
R=C.count("R")
ans=R
for i in range(N):
    
    if C[i]=="R":
        R-=1
    else:
        W+=1
    if  ans>max(W,R):
        ans=max(W,R)
print(ans)
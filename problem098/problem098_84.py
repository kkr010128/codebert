n=int(input())
A=list(input())
w=0 ; r=A.count("R") ; ans=10**7
for i in range(n+1):
    ans=min(ans, max(w,r))
    if i==n:print(ans);exit()
    if A[i]=="R":
        r-=1
    else:
        w+=1

n=int(input())
S=[int(i) for i in input().split()]
q=int(input())
T=[int(i) for i in input().split()]


def solve(i,m,n,S):
    if sum(S)<m:
        return False
        
    if m==0:
        return True

    elif i>=n:
        return False
        
    res=solve(i+1,m,n,S) or solve(i+1,m-S[i],n,S)
    return res
    
for i in range(q):
    attempt=solve(0,T[i],n,S)
    if attempt:
        print("yes")
        
    else:
        print("no")

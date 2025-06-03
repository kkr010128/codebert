import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n,k=map(int,input().split())
    A=list(map(int,input().split()))

    for i in range(k):
        B=[0]*(n+1)

        for j in range(n):
            val=A[j]
            B[max(0,j-val)]+=1
            B[min(n,j+val+1)]-=1
        
        for k in range(n):
            B[k+1]+=B[k]
        A=B[:-1]

        if A==[n]*(n):
            break
    
    

    print(*A)    
    
resolve()
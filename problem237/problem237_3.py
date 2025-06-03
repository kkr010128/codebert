import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    N=int(input())
    A=[]
    for i in range(N):
        X,L=map(int,input().split())

        A.append([X-L,X+L])

    A=sorted(A, key=lambda x: x[1])
    cur=-(10**10)
    cnt=0
    for i in range(N):
        if A[i][0]<cur: continue
        else:
            cur=A[i][1]
            cnt+=1
    print(cnt)



    
    

    
resolve()
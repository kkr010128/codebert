N=int(input())
A=list(map(int,input().split()))
SUM=sum(A)
Q=int(input())
List=[0 for _ in range(10**5+1)]
for a in A:
    List[a]+=1
for q in range(Q):
    B,C=map(int,input().split())
    SUM-=B*List[B]
    SUM+=C*List[B]
    List[C]+=List[B]
    List[B]=0
    print(SUM)
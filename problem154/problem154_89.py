#B
N, K=map(int,input().split())
d=[]
A=[]
for i in range(K):
    di=int(input())
    Ai=list(map(int,input().split()))
    d.append(di)
    A.append(Ai)
A_all=[]
for i in A:
    for j in i:
        A_all.append(j)
A_set=list(set(A_all))
print(N-len(A_set))
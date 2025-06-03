
A,B,N=map(int,input().split())

def func(t):
    return int(t)

#NはBより大きいかもしれないし小さいかもしれない
#B-1が最高だが、NがB-1より小さいとどうしようもない
x=min(B-1,N)
print(func(A*x/B)-A*func(x/B))
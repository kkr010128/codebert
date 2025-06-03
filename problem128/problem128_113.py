X,N=map(int,input().split())
P=set(map(int,input().split()))
l=[0]+[(1+i//2)*(-1 if i%2==0 else 1) for i in range(101)]
for i in l:
    if X+i not in P:
        print(X+i)
        break
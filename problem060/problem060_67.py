n,m,l=map(int,input().split())
A = [tuple(map(int,input().split())) for _ in range(n)]
B = [tuple(map(int,input().split())) for _ in range(m)]
BT = tuple(map(tuple,zip(*B)))
for a in A:
    temp=[]
    for b in BT:
        temp.append(sum([x*y for (x,y) in zip(a,b)]))
    print(*temp)
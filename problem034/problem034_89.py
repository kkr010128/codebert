n=list(map(int,input().split()))
p=['2354','3146','2651','1562','1364','2453']
for _ in range(int(input())):
    t,m=map(int,input().split())
    t=n.index(t)
    m=str(n.index(m)+1)
    print(n[int(p[t][(p[t].index(m)+1)%4])-1])

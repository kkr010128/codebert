N,K=map(int,input().split())
P=list(map(int,input().split()))
C=list(map(int,input().split()))
P=[i-1 for i in P]
idle_max=-10**27



for s in range(0,N):
    k=K-1
    score=0
    s=P[s]
    score+=C[s]
    count=1
    idle_max=max(idle_max,score)
    visited={s:[count,score]}
    while k and not P[s] in visited:

        k-=1
        count+=1
        s=P[s]
        score+=C[s]
        visited[s]=[count,score]

        idle_max=max(idle_max,score)
    #print(visited)
    if k:
        c1,score1=visited[s]
        c2,score2=visited[P[s]]
        c1+=1
        s=P[s]
        score1+=C[s]
        score+=C[s]
        k-=1


        n=c1-c2
        score+=(score1-score2)*(k//n)
        k%=n
        idle_max=max(idle_max,score)
    while k:
        k-=1
        s=P[s]
        score+=C[s]
        idle_max=max(idle_max,score)


print(idle_max)

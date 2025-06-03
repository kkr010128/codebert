def main():
    n=int(input())
    u,k,v=0,0,[[] for _ in range(n+1)]
    for i in range(n):
        l=list(map(int,input().split()))
        u=l[0]
        for j in l[2:]:
            v[u].append(j)
    d=[0]*(n+1)
    f=[0]*(n+1)

    def dfs(s,t):
        d[s]=t
        for i in v[s]:
            if d[i]==0:
                t=dfs(i,t+1)
        f[s]=t+1
        return t+1

    s,t=1,1
    while 0 in d[1:]:
        T=dfs(s,t)
        for i in range(1,n+1):
            if d[i]==0:
                s=i
                t=T+1
                break

    for i in range(1,n+1):
        print(i,d[i],f[i])

if __name__ == '__main__':
    main()

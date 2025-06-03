from collections import deque
def main():
    N,M,*AB=map(int,open(0).read().split())
    g=[[] for _ in range(N+1)]
    for a,b in zip(*[iter(AB)]*2):
        g[a].append(b)
        g[b].append(a)
    q=deque([1])
    s=[0]*(N+1)
    s[1]=1
    while q:
        u=q.popleft()
        for v in g[u]:
            if not s[v]:
                s[v] = u
                q.append(v)
    print("Yes")
    print("\n".join(map(str, s[2:])))
if __name__ == "__main__":
    main()
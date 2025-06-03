
def main():
    N, M, X = map(int,input().split())
    
    cost = []
    effect = []
    for _ in range(N):
        t = list(map(int,input().split()))
        cost.append(t[0])
        effect.append(t[1:])

    res = float("inf")
    for bits in range(1<<N):
        f = True
        total = 0
        ans = [0] * M
        for flag in range(N):
            if (1<< flag) & (bits):
                total += cost[flag]
                for idx, e in enumerate(effect[flag]):
                    ans[idx] += e 
        for a in ans:
            if a < X: f = False
        if f:
            res = min(res, total)

    print(res if res != float("inf") else -1)

if __name__ == "__main__":
    main()


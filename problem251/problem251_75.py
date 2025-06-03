N, K = map(int, input().split())
A = tuple(map(int, input().split()))
T = input()

bestmove = {'r':2, 's':0, 'p':1}

ans = 0
for k in range(K):
    t = T[k::K]
    prev = -1
    for opp in t:
        me = bestmove[opp]
        if prev != me:
            prev = me
            ans += A[me]
        else:
            prev = -1

print(ans)

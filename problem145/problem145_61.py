def resolve():
    N, M = list(map(int, input().split()))
    AB = {}
    for _ in range(M):
        a, b = list(map(int, input().split()))
        a, b = a-1, b-1
        if a not in AB:
            AB[a] = []
        if b not in AB:
            AB[b] = []
        AB[a].append(b)
        AB[b].append(a)

    import collections
    q = collections.deque([0])
    passed = [-1 for i in range(N)]
    passed[0] = 0
    while q:
        node = q.pop()
        for nxt in AB[node]:
            if passed[nxt] == -1:
                passed[nxt] = node
                q.appendleft(nxt)
    #print(metrics)
    for m in passed:
        if m == -1:
            print("No")
            return
    print("Yes")
    for i in range(1, N):
        print(passed[i]+1)


if '__main__' == __name__:
    resolve()
def resolve():
    import itertools
    N = int(input())
    A = []
    X = []
    ans = [0]
    for _ in range(N):
        a = int(input())
        xx = []
        for __ in range(a):
            x = list(map(int, input().split()))
            xx.append(x)
        X.append(xx)
        A.append(a)
    for i in itertools.product([0, 1], repeat=N):
        flag = 0
        for p in range(N):
            for q in range(A[p]):
                if i[p] == 1 and X[p][q][1] != i[X[p][q][0]-1]:
                    flag = 1
        if flag == 0:
            ans.append(i.count(1))
    print(max(ans))
resolve()
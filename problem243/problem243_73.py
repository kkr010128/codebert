def resolve():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        S, T = input().split()
        s.append(S)
        t.append(int(T))
    X = input()
    print(sum(t[s.index(X)+1:]))
resolve()
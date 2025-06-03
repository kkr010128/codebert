N, S = open(0).read().split()
S = list(map(int, list(S)))
N = int(N)

cnt = 0
for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                try:
                    n = S.index(i)
                    m = S[n+1:].index(j)
                    o = S[n+m+2:].index(k)
                    cnt += 1
                except ValueError:
                    pass
print(cnt)
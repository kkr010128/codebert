D, *I = map(int, open(0).read().split())
C, S, T = I[:26], list(zip(*[iter(I[26:-D])] * 26)), I[-D:]

last = [0] * 26
ans = 0
for d, i in enumerate(T, 1):
    ans += S[d - 1][i - 1]
    last[i - 1] = d
    ans -= sum(c * (d - l) for c, l in zip(C, last))
    print(ans)
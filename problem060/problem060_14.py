from itertools import islice

def make_seq():
    n, m, l = list(map(int, input().split()))

    m1 = [list(map(int, input().split())) for _ in range(n)]
    m2 = [list(map(int, input().split())) for _ in range(m)]

    def g():
        for r1 in m1:
            for r2 in zip(*m2):
                yield str(sum(i*j for i, j in zip(r1, r2)))

    return (n, l, list(g()))

n, l, lst = make_seq()
for i in range(n):
    print(" ".join(islice(lst, i*l, (i+1)*l)))
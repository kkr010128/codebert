n_max, m_max, l_max = (int(x) for x in input().split())
a = []
b = []
c = []

for n in range(n_max):
    a.append([int(x) for x in input().split()])

for m in range(m_max):
    b.append([int(x) for x in input().split()])

for n in range(n_max):
    c.append( [sum(a[n][m] * b[m][l] for m in range(m_max)) for l in range(l_max)])

for n in range(n_max):
    print(" ".join(str(c[n][l]) for l in range(l_max)))
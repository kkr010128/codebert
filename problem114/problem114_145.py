D = int(input())
c = [*map(int, input().split())]
s = [0] + [[*map(int, input().split())] for _ in range(D)]
t = [0] + [int(input()) for _ in range(D)]

v = 0
last = [0] * 26
for d in range(1, D+1):
    select = t[d] - 1
    v += s[d][select]
    last[select] = d
    v -= sum(c[i] * (d - last[i]) for i in range(26))
    print(v)

# coding: utf-8

n, m = map(int, input().split())
total = [0] * m

for i in range(n+1):
    if i < n:
        line = [int(j) for j in input().split()]
        print(" ".join([str(k) for k in line]),sum(line))
        total = [total[i] + line[i] for i in range(m)]
    else:
        print(" ".join([str(k) for k in total]),sum(total))
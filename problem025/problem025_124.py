import itertools as itl

n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))
S = []

for i in range(n):
    cmb = list(itl.combinations(A, i+1))
    for j in cmb:
        S.append(sum(j))

for m in M:
    flg = False
    for s in S:
        if s == m:
            flg = True
            break
    if flg:
        print("yes")
    else:
        print("no")


from sys import stdin

input = stdin.readline

n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

set_m = set([])

for i in range(2 ** n):
    tmp = 0
    for j in range(n):
        if (i >> j) & 1:
            tmp += A[j]

    set_m.add(tmp)

for i in m:
    if i in set_m:
        print("yes")
    else:
        print("no")


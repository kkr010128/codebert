import heapq
import sys
input = sys.stdin.readline
n = int(input())
sss = [input()[:-1] for _ in range(n)]

a = []
b = []
ss = 0
ii = 0
for i in sss:
    mi = 0
    ma = 0
    s = 0
    for j in i:
        if j == "(":
            s += 1
        else:
            s -= 1
        mi = min(mi, s)
        ma = max(ma, s)
    ss += s
    if s >= 0:
        a.append([s, mi, ma, ii])
    else:
        mi = 0
        ma = 0
        s = 0
        for j in reversed(i):
            if j == ")":
                s += 1
            else:
                s -= 1
            mi = min(mi, s)
            ma = max(ma, s)
        b.append([s, mi, ma, ii])
    ii += 1


if ss != 0:
    print("No")
    exit()
a.sort(reverse=1, key=lambda x: x[1])
b.sort(reverse=1, key=lambda x: x[1])


def ok(a):
    s = 0
    for i, j, _, _ in a:
        if s + j < 0:
            print("No")
            exit()
        s += i

ok(a)
ok(b)
print("Yes")

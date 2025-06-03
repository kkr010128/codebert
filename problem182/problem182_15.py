import sys

stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

n, k, c = nm()
a = ns()

ans = []
al = []
count = 0
dey = 1
for i in a:
    if i is "o" and count <= 0:
        al.append(dey)
        count = c + 1
    dey += 1
    count -= 1
ar = []
count = 0
dey = n
for i in reversed(a):
    if i is "o" and count <= 0:
        ar.append(dey)
        count = c + 1
    dey -= 1
    count -= 1


al = al[:k]
ar = ar[:k]
for i in al:
    j = ar.pop(-1)
    if i == j:
        ans.append(i)
for i in ans:
    print(i)

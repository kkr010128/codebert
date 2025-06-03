import sys
sys.setrecursionlimit(200001)

N, M = [int(n) for n in input().split()]
S = input()

p1 = False
x1 = 0
m1 = N
c1 = 0
for n in S:
    if n == "1":
        if p1:
            c1 += 1
        else:
            c1 = 1
            p1 = True
    else:
        p1 = False
        if c1 > 0:
            if c1 > x1:
                x1 = c1
            if c1 < m1:
                m1 = c1
           
def rest(l, ans):
    s = M
    while s > 0:
        if s >= l:
            ans.append(l)
            return ans
        if S[l-s] == "1":
            if s == 1:
                return -1
            s -= 1
            continue
        l -= s
        if rest(l, ans) == -1:
            s -= 1
        else:
            ans.append(s)
            return ans
    return -1

if x1 > M - 1:
    ans = -1
else:
    ans = rest(N, [])

if ans == -1:
    print(-1)
else:
    print(" ".join([str(n) for n in ans]))
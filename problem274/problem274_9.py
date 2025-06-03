from bisect import *
n,m = map(int,input().split())
S = input()
ok = []
for i,s in enumerate(S[::-1]):
    if s == '0':
        ok.append(i)

now = 0
ans = []
while now != n:
    nxt = ok[bisect_right(ok, now + m) - 1]
    if nxt == now:
        ans = [str(-1)]
        break
    else:
        ans.append(str(nxt - now))
        now = nxt
print(' '.join(ans[::-1]))

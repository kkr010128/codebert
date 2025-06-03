from collections import deque
# end,cnt
dq = deque()

(n,d,a),*xh = [list(map(int, s.split())) for s in open(0)]
xh.sort()

total_bomb = 0
eff_bomb = 0

for x,h in xh:
    while dq and dq[0][0] < x:
        end, cnt = dq.popleft()
        eff_bomb -= cnt
    resid = h - eff_bomb * a
    if resid > 0:
        cnt = 0--resid//a
        end = x + 2 * d
        dq.append((end,cnt))
        eff_bomb += cnt
        total_bomb += cnt

print(total_bomb)
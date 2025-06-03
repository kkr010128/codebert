from collections import defaultdict
import bisect

N = int(input())
S = input()
# s2i = [[] for i in range(10)]
s2i = defaultdict(list)

for i, si in enumerate(S):
    s2i[si] += [i]

ans = 0

for i in range(1000):
    pin = str(i).zfill(3)
    ii = -1
    flag = True
    for p in pin:
        s2ip = s2i[p]
        if s2ip:
            iii = bisect.bisect_right(s2ip, ii)
            if iii == len(s2ip):
                flag = False
                break
            ii = s2ip[iii]
        else:
            flag = False
            break
    if flag:
        ans += 1

print(ans)

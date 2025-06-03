from collections import OrderedDict
import sys

cnt = OrderedDict()
for i in range(ord('a'), ord('z') + 1):
    cnt[chr(i)] = 0

S = sys.stdin.readlines()
for s in S:
    s = s.lower()
    for i in s:
        if i in cnt:
            cnt[i] += 1

for k, v in cnt.items():
    print('{} : {}'.format(k, v))
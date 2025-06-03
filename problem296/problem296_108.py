import sys
input = sys.stdin.readline

s = list(input().rstrip())
k = int(input())
n = len(s)

group = []

cnt = 0

from collections import Counter
c = Counter(s)
if len(c) == 1:
    print(n*k//2)
    sys.exit()

for i in range(n):
    if i == 0:
        cnt += 1
        continue
    elif i == n - 1:
        if s[i] == s[i - 1]:
            cnt += 1
            group.append(cnt)
        else:
            group.append(cnt)
            group.append(1)
        continue
    
    if s[i] == s[i - 1]:
        cnt += 1
    else:
        group.append(cnt)
        cnt = 1
ans = 0
if k == 1:
    for i in group:
        ans += i//2
    print(ans)
    sys.exit()
from copy import deepcopy
first = deepcopy(group)
last = deepcopy(group)
if s[0] == s[-1]:
    first[-1] += last[0]
    last[0] = 0

for i in first:
    ans += i//2
for i in last:
    ans += i//2
if k == 2:
    print(ans)
    sys.exit()
mid = deepcopy(first)
if s[0] == s[-1]:
    mid[0] = 0
temp = 0
for i in mid:
    temp += i//2
ans += temp*(k - 2)
print(ans)



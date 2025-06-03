n = int(input())
a = list(map(int,input().split()))

import collections
count = collections.Counter(a)

import math
def p(n, r):
    return math.factorial(n) // math.factorial(n - r)
def c(n, r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# print(count)
s = 0
cmb = {}
for i in count.keys():
    cmb[i] = (c(count[i], 2),c(count[i] - 1, 2))
    s += cmb[i][0]
# print(s)
# print(cmb)

for i in range(n):
    ans = s - cmb[a[i]][0] + cmb[a[i]][1]
    print(ans)
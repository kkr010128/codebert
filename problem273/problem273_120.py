import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
def cumsum(a):
    """※ aを破壊する
    l[i] = sum(a[:i]) なるlを返す
    sum(a[i:j]) == l[j+1] - l[i]
    """
    c = 0
    n = len(a)
    a.insert(0, 0)
    for i in range(1, n+1):
        a[i] = a[i-1]+a[i]
    return a
a = cumsum(a)
aa = [((item - i)%k) for i,item in enumerate(a)]
ans = 0
from collections import defaultdict
c = defaultdict(int)
for i in range(min(k, len(aa))):
    c[aa[i]] += 1
for i,item in enumerate(aa):
    c[item] -= 1
#     print(c, item)
    ans += c[item]
    if i+k<n+1:
        c[aa[i+k]] += 1
print(ans)
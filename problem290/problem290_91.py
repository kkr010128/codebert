import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort(reverse=True)
def sub(x):
    val = 0
    for aa,ff in zip(a,f):
        val += max(0, aa - (x//ff))
    return val<=k
if sub(0):
    ans = 0
else:
    l = 0
    r = sum(aa*ff for aa,ff in zip(a,f))
    while l+1<r:
        m = (l+r)//2
        if sub(m):
            r = m
        else:
            l = m
    ans = r
print(ans)
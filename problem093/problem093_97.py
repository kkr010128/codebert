from sys import stdin
n,k = map(int,stdin.readline().split())
p = list(map(int,stdin.readline().split()))
c = list(map(int,stdin.readline().split()))

ans = -float("inf")
def helper(index):
    visited  = {index}
    looplen = 1
    looptotal = c[index]
    while p[index]-1 not in visited:
        nextindex = p[index] - 1
        looplen += 1
        looptotal += c[nextindex]
        visited.add(nextindex)
        index = nextindex
    return (looplen,looptotal)

for i in range(n):
    looplen,looptotal = helper(i)
    if looptotal >= 0:
        cur = looptotal*((k//looplen)-1) if k >= looplen else 0
        remain = looplen + (k%looplen) if k >= looplen else k
    else:
        cur = 0
        remain = looplen
    curmax = -float("inf")
    curindex = i
    for _ in range(remain):
        nextindex = p[curindex]-1
        cur += c[nextindex]
        curmax = max(curmax,cur)
        curindex = nextindex
    ans = max(ans,curmax)
print(ans)
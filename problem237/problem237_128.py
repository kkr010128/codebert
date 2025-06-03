import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
lr = [None]*n
for i in range(n):
    x,l = map(int, input().split())
    lr[i] = (x-l, x+l)
lr.sort(key=lambda x: x[1])
ans = 0
c = -10**10
for l,r in lr:
    if c<=l:
        ans += 1
        c = r
print(ans)